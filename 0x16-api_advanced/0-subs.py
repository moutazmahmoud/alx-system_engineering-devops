#!/usr/bin/python3
"""
This script defines a function that interacts with the Reddit API
to return the number of subscribers for a specified subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the total number of subscribers for a given subreddit.

    If the subreddit is invalid, the function returns 0.
    Note that the function ensures it does not follow redirects, 
    which can occur with invalid subreddit names.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': 'MyRedditAPI/1.0 (by /u/yourusername)'
    }
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        return data['data'].get('subscribers', 0)
    
    return 0


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass a subreddit name as an argument.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
