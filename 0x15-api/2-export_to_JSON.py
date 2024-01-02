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
    todo_url = url + 'todos'
    todos = requests.get(todo_url).json()
    list_todos = []

    for todo in todos:
        todos_dict = {"task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": name}
        list_todos.append(todos_dict)
        dictt = {u_id: list_todos}
    with open('{}.json'.format(u_id), 'w') as file:
        json.dump(dictt, file)
