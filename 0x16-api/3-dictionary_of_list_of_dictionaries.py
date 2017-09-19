#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format
"""
import json
import requests
import sys


def getEmployeeDetails():
    """ to retrive employee todo list"""
    urlTodo = "https://jsonplaceholder.typicode.com/todos/"
    urlUsers = "https://jsonplaceholder.typicode.com/users/"
    reqTodo = requests.get(urlTodo)
    reqUsers = requests.get(urlUsers)
    taskList = []

    for user in reqUsers.json():
        for task in reqTodo.json():
            tempDict = {}
            tempDict['task'] = task.get("title")
            tempDict['completed'] = task.get("completed")
            tempDict['username'] = user.get("name")
            taskList.append(tempDict)
            uid = user.get("id")

    jsonFile = "todo_all_employees.json"
    with open(jsonFile, 'w') as f:
        json.dump({uid: taskList}, f)


if __name__ == "__main__":
    getEmployeeDetails()
