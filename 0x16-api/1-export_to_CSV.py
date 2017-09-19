#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format
"""
import csv
import requests
import sys


def getEmployeeDetails(uid):
    """ to retrive employee todo list"""
    urlTodo = "https://jsonplaceholder.typicode.com/todos"
    urlUsers = "https://jsonplaceholder.typicode.com/users"
    reqTodo = requests.get(urlTodo)
    reqUsers = requests.get(urlUsers)
    doneTaskList = []

    for task in reqTodo.json():
        if task.get('userId') == uid:
            for user in reqUsers.json():
                if user.get('id') == uid:
                    doneTaskList.append([uid, user.get('username'),
                                        task.get('completed'),
                                        task.get('title')])
    csvFile = "{}.csv".format(uid)
    with open(csvFile, 'w') as f:
        writr = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in doneTaskList:
            writr.writerow(task)

if __name__ == "__main__":
    try:
        getEmployeeDetails(int(sys.argv[1]))
    except:
        print("provide an id")
