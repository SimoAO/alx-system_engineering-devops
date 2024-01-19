#!/usr/bin/python3
"""
number of subscribers module
"""
import requests


def number_of_subscribers(subreddit):
    """number of subscribers class"""
    url = "https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyReddit0"}
    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp.status_code == 200:
        return resp.json().get('data').get('subscribers')
    else:
        return 0
