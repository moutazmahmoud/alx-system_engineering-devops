#!/usr/bin/python3
"""
number of subscribers
"""

from requests import get


def number_of_subscribers(subreddit):
   

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': ''}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
