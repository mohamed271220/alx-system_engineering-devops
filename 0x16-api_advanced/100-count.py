#!/usr/bin/python3
"""
This module contains the function count_words.
The function fetches all hot posts from a given subreddit and counts the occurrence of given keywords in the titles.
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
            word_dict[word.lower()] = word_dict.get(word.lower(), 0)

    if after is None:
        sorted_dict = sorted(word_dict.items(),
                             key=lambda x: (-x[1], x[0]))
        for word, count in sorted_dict:
            if count > 0:
                print(f'{word}: {count}')
        return None

    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'user-agent': 'redquery'}
    params = {'limit': 100, 'after': after}
    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code != 200:
            return None
        data = response.json().get('data', {})
        posts = data.get('children', [])
        after = data.get('after', '')
        for post in posts:
            title = post.get('data', {}).get('title', '')
            words_in_title = title.lower().split()
            for word in word_dict.keys():
                word_dict[word] += words_in_title.count(word)
        return count_words(subreddit, word_list, after, word_dict)
    except requests.exceptions.RequestException:
        return None
