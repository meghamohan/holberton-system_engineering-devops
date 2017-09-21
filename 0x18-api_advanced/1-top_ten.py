#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
        prints the titles of the first 10 hot posts listed
        for a given subreddit
    """
    count = 0
    myList = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    req = requests.get(url, headers={'user-agent': 'Task1'})
    try:
        for data in req.json().get('data').get('children'):
            myList.append(data.get('data').get('title'))
            count += 1
            if count > 9:
                break
        print("\n".join(x for x in myList))
    except:
        print("None")
