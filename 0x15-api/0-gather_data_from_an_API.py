#!/usr/bin/python3
""" TO DO list information/progress module """
import requests
import sys


if __name__ == '__main__':
    """ TO DO list class """

    u_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user_url = url + 'users/{}'.format(u_id)
    info = requests.get(user_url).json()
    name = info.get('name')
    todo_url = url + 'todos'
    todos = requests.get(todo_url).json()
    todo_tot = 0
    todo_comp = 0
    tot_comp = []

    for todo in todos:
        if todo.get('userId') == int(u_id):
            todo_tot += 1
            if todo.get('completed') is True:
                todo_comp += 1
                tot_comp.append(todo.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(
        name, todo_comp, todo_tot))
    for task in tot_comp:
        print('\t {}'.format(task))
