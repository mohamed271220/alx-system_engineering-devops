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
    headers = {"User-Agent": "Python/requests:subreddit.\
        subscriber.count:v1.0 (by /u/specter)"}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get('data', {}).get('children', [])
    for post in data:
        print(post.get('data', {}).get('title'))
