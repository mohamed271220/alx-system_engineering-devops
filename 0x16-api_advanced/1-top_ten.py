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
    user = {'User-Agent': 'Lizzie'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    try:
        response = requests.get(url, headers=user).json()
        posts = response.get('data', {}).get('children', [])
        for post in posts:
            print(post.get('data', {}).get('title'))
    except requests.exceptions.RequestException:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
