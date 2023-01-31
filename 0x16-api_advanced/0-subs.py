#!/usr/bin/python3
"""

Function the queris the Reddit API and
return the number of subscribers
for a given subreddit 
"""

import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url, headers={'User-Agent': 'Python/requests})

    try:
       resp = req.json()
       return resp.get("data", {}).get("subscribers", 0)
except Exception:
       return 0
