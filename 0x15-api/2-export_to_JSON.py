#!/usr/bin/python3
""" TO DO list information/progress module """
import requests
import sys
import json


if __name__ == '__main__':
    """ JSON format data exporting class """

    u_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user_url = url + 'users/{}'.format(u_id)
    info = requests.get(user_url).json()
    name = info.get('username')
    u_json = {}
    todo_url = url + 'todos'
    todos = requests.get(todo_url).json()
    dictt = {u_id: []}

    with open('{}.json'.format(u_id), 'w+') as file:
        for todo in todos:
            dictt[u_id].append({"task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": name})
            json.dump(dictt, file)
