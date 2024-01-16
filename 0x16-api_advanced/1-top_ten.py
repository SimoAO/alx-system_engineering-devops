#!/usr/bin/python3
"""
top ten module
"""
import requests


def top_ten(subreddit):
    """top ten class"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(
            subreddit)
    head = {"User-Agent": "MyReddit0"}
    resp = requests.get(url, headers=head, allow_redirects=False)
    if resp.status_code == 200:
        for post in resp.json().get('data').get('children'):
            print(post.get('data').get('title'))
    else:
        print("None")
