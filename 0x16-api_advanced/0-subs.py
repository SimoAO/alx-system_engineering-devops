#!/usr/bin/python3
"""number of subscribers module"""
import requests


def number_of_subscribers(subreddit):
    """number of subscribers class"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    head = {"User-Agent": "MyReddit0"}
    resp = requests.get(url, headers=head, allow_redirects=False)

    if resp.status_code == 200:
        return resp.json().get("data").get("subscribers")
    elif resp.status_code == 302:
        return 0
    else:
        return "OK"
