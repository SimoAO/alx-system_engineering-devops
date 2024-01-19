#!/usr/bin/python3
"""
top ten module
"""
import requests


def top_ten(subreddit):
    """top ten class"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyReddit0"}
    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp.status_code == 200:
        for post in resp.json().get('data').get('children'):
            print(post.get('data').get('title'))
    else:
        print("None")
