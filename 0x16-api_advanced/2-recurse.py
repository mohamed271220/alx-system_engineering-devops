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
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        results = response.json().get("data")
        after = results.get("after")
        count += results.get("dist")
        posts = results.get("children", [])
        for post in posts:
            hot_list.append(post.get("data", {}).get("title"))
        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
    except requests.exceptions.RequestException:
        return None
