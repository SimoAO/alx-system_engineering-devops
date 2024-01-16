#!/usr/bin/python3
"""
recurse module
"""
import requests


def recurse(subreddit, hot_list=[]):
    """recurse class"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(
            subreddit)
    head = {"User-Agent": "MyReddit0"}
    params = {"after": after}
    resp = requests.get(url, headers=head, params = params,
            allow_redirects=False)
    if resp.status_code == 200:
        after = req.json().get('data').get('after')
        for post in resp.json().get('data').get('children'):
            hot_list.append(post.get('data').get('title'))
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
