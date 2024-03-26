#!/usr/bin/python3
"""
This python script is sing th I, for a given employee ID,
returns information O list progress.
"""


import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}"
            .format(userId))
    name = user.json().get('name')

    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    totalTasks = 0
    completedTasks = 0

    for task in todos.json():
        if task.get('userId') == int(userId):
            totalTasks += 1
            if task.get('completed'):
                completedTasks += 1
    print("Employee {} is done with tasks({}/{}):".format(
        name, completedTasks, totalTasks))
    print('\n'.join(["\t " + task.get('title') for task in todos.json(
            ) if task.get(
                'userId') == int(userId) and task.get('completed')]))
