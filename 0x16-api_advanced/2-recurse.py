#!/usr/bin/python3
"""
This module contains the function recurse.
The function fetches all hot posts from a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Fetches and returns a list of titles of all hot posts for a given subreddit.
    If the subreddit does not exist or an error occurs, it returns None.
    """
    if hot_list is None:
        hot_list = []

    headers = {"User-Agent": "my-app/0.0.1"}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after, "limit": 100}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    after = data.get("after", None)
    children = data.get("children", [])

    for child in children:
        hot_list.append(child.get("data", {}).get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
