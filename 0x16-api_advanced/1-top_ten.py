#!/usr/bin/python3
"""returns the number of subscribers"""
import requests


def top_ten(subreddit):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    resp = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                        .format(subreddit),
                        headers=headers,
                        allow_redirects=False)

    if resp.status_code == 200:
        resp = resp.json()
        for child in resp.get('data').get('children'):
            print(child.get('data').get('title'))
    else:
        print(None)
        return 0
