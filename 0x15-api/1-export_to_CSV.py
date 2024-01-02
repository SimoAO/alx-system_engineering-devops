#!/usr/bin/python3
""" TO DO list information/progress module """
import csv
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

    with open('{}.csv'.format(u_id), 'w', newline='') as file:
        csv_w = csv.writer(file)

        for todo in todos:
            csv_w.writerow([
                u_id, name, todo.get('completed'), todo.get('title')
                ])
