#!/usr/bin/python3
"""
count wordds module
"""
import requests


def count_words(subreddit, word_list, hot_list=None, after=None):
    """count words class"""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyReddit0"}
    params = {"after": after}
    resp = requests.get(
            url, headers=headers, params=params, allow_redirects=False
            )

    if resp.status_code == 200:
        after = resp.json().get('data').get('after')
        for post in resp.json().get('data').get('children'):
            hot_list.append(post.get('data').get('title'))

        if after is not None:
            return count_words(subreddit, word_list, hot_list, after)
        else:
            return hot_list
    else:
        return None


def count_words(subreddit, word_list):
    hot_list = count_words(subreddit)
    if hot_list is None:
        return

    word_count = {}
    for post_title in hot_list:
        words = post_title.lower().split()
        for word in words:
            word = word.rstrip('.,!?;:"()[]{}')
            if word in word_list:
                word_count[word] = word_count.get(word, 0) + 1

    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_word_count:
        print(f"{word}: {count}")
