#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format
"""
import json
import requests
import sys


def getEmployeeDetails(uid):
    """ to retrive employee todo list"""
    urlTodo = "https://jsonplaceholder.typicode.com/todos"
    urlUsers = "https://jsonplaceholder.typicode.com/users"
    reqTodo = requests.get(urlTodo)
    reqUsers = requests.get(urlUsers)
    taskList = []

    for task in reqTodo.json():
        if task.get('userId') == uid:
            for user in reqUsers.json():
                if user.get('id') == uid:
                    tempDict = {}
                    tempDict['task'] = task.get("title")
                    tempDict['completed'] = task.get("completed")
                    tempDict['username'] = user.get("name")
                    taskList.append(tempDict)

    jsonFile = "{}.json".format(uid)
    with open(jsonFile, 'w') as f:
        json.dump({uid: taskList}, f)


if __name__ == "__main__":
    try:
        getEmployeeDetails(int(sys.argv[1]))
    except:
        print("provide an id")
