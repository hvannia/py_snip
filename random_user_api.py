# Requires 
import requests


def get_user(version="1.3"):
    """Get random users"""
    url = f"https://randomuser.me/api/{version}/?results=1"
    response = requests.get(url)
    if response:
        return response.json()["results"][0]


# eaxct same user use seed
#url = f"https://randomuser.me/api/{version}/?results=1&seed=310"



