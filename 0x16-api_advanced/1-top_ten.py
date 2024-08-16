#!/usr/bin/python3
'''
    This module contains the function top_ten.
    The function fetches the top ten hot
    posts from a given subreddit.
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
        Fetches and prints the titles of the top ten hot posts
        for a given subreddit.
        If the subreddit does not exist or an error occurs,
        it prints None.
    '''
    headers = {"User-Agent": "my-app/0.0.1"}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get('data', {}).get('children', [])
    for post in data[:10]:
        print(post.get('data', {}).get('title'))


if __name__ == "__main__":
    top_ten(argv[1])
