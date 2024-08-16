#!/usr/bin/python3
"""
queries subscribers on a given Reddit subreddit.
"""

import requests
from sys import argv


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Python/requests:subreddit.\
        subscriber.count:v1.0 (by /u/specter)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        return 0



if __name__ == "__main__":
    number_of_subscribers(argv[1])
