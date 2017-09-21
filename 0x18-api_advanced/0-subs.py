#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
        queries the Reddit API and returns the number of subscribers
    """
    if subreddit is None:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url, headers={'user-agent': 'Chrome'})
    if req.status_code is not 200:
        return 0
    return req.json()['data']['subscribers']
