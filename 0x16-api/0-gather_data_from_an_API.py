#!/usr/bin/python3
"""
for a given employee ID, returns information about his/her TODO list progress.
"""
import requests
import sys


def getEmployeeDetails(uid):
    """ to retrive employee todo list"""
    url = "https://jsonplaceholder.typicode.com/todos"
    req = requests.get(url)
    allTasks = 0
    doneTasks = 0
    doneTaskList = []
    for task in req.json():
        if task.get('userId') == uid:
            allTasks += 1
            if task.get('completed'):
                doneTasks += 1
                doneTaskList.append(task.get('title'))
    url = "https://jsonplaceholder.typicode.com/users/"
    req = requests.get(url)
    for emp in req.json():
        if emp.get('id') == uid:
            print("Employee {} is done with tasks({}/{}):".
                  format(emp.get("name"), doneTasks, allTasks))
    for task in doneTaskList:
        print("\t {}".format(task))


if __name__ == "__main__":
    try:
        getEmployeeDetails(int(sys.argv[1]))
    except:
        print("provide an id")
