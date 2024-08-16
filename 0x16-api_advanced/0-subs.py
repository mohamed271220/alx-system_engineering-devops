#!/usr/bin/python3
"""
queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except (requests.exceptions.RequestException, KeyError):
        return 0
