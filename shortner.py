import requests
from config import SHORTENER_URL, SHORTENER_API

def shorten_link(url):
    try:
        data = {"api_key": SHORTENER_API, "url": url}
        res = requests.post(SHORTENER_URL, json=data, timeout=10).json()
        if res.get("status") == "success":
            return res.get("shortened_url")
        return url
    except:
        return url
