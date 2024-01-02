#!/usr/bin/python3
""" TO DO list information/progress module """
import requests
import sys


if __name__ == '__main__':
    """ CSV data exporting class """

    u_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user_url = url + 'users/{}'.format(u_id)
    info = requests.get(user_url).json()
    name = info.get('username')
    todo_url = url + 'todos'
    todos = requests.get(todo_url).json()

    with open('{}.csv'.format(u_id), 'w') as file:
        for todo in todos:
            file.write('"{}","{}","{}","{}"\n'
                    .format(u_id, name, todo.get('completed'),
                            todo.get('title')))
