#!/usr/bin/python3
""" TO DO list information/progress module """
import json
import requests


if __name__ == '__main__':
    """ JSON format data exporting class """

    url = 'https://jsonplaceholder.typicode.com/'
    user_url = url + 'users'
    info = requests.get(user_url).json()
    todo_url = url + 'todos'
    todos = requests.get(todo_url).json()
    list_todos = []

    with open('todo_all_employees.json', 'w') as file:
        u_json = {}
        for user in info:
            name = user.get('username')

            tasks = []
            for todo in todos:
                if todo.get('userId') == user.get('id'):
                    task = {}
                    task['username'] = name
                    task['task'] = todo.get('title')
                    task['completed'] = todo.get('completed')
                    tasks.append(task)
                u_json[str(user.get('id'))] = tasks
        file.write(json.dumps(u_json))
