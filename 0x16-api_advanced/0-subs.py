#!/usr/bin/python3
"""returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    resp = requests.get('https://www.reddit.com/r/{}/about/.json'
                        .format(subreddit),
                        headers=headers,
                        allow_redirects=False)
    if resp.status_code == 200:
        resp = resp.json()
        data = resp.get('data')
        return data.get('subscribers')
    return 0
