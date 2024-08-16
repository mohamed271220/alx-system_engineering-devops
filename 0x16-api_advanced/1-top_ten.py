#!/usr/bin/python3
'''
    This module contains the function top_ten.
    The function fetches the top ten hot
    posts from a given subreddit.
'''
import requests
from sys import argv


def top_ten(subreddit):
    # Set the URL for the subreddit's hot posts JSON endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Set a custom User-Agent to avoid getting blocked by Reddit's API
    headers = {"User-Agent": "Python/requests:subreddit.hot.posts:v1.0 (by /u/yourusername)"}
    
    # Perform the GET request without following redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        
        # Print the title of each post
        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        # If the subreddit is invalid or the request failed, print None
        print(None)
        return


if __name__ == "__main__":
    top_ten(argv[1])
