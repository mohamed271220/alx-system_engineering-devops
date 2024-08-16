#!/usr/bin/python3
"""
This module contains the function count_words.
The function fetches all hot posts from a given
subreddit and counts the occurrence of given keywords in the titles.
"""
import requests


def count_words(subreddit, word_list, after='', word_dict={}):
    """
    Fetches all hot posts from a given subreddit,
    parses the titles, and counts the occurrence of given keywords.
    The keywords are case-insensitive and delimited by spaces.
    The function prints a sorted count of the keywords.
    If no posts match or the subreddit is invalid,
    it prints nothing.
    """

    if not word_dict:
        for word in word_list:
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 0

    if after is None:
        wordict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word in wordict:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {"User-Agent": "Python/requests:subreddit.\
        subscriber.count:v1.0 (by /u/specter)"}
    parameters = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=parameters,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        hot = response.json()['data']['children']
        aft = response.json()['data']['after']
        for post in hot:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]

            for word in word_dict.keys():
                word_dict[word] += lower.count(word)

    except Exception:
        return None

    count_words(subreddit, word_list, aft, word_dict)
