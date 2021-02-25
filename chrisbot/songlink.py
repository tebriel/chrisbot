"""Handle Songlink Stuff"""
import os
from typing import Optional

import requests
from urlextract import URLExtract


EXTRACTOR = URLExtract()


def extract_link(text: str) -> Optional[str]:
    """Extract the URL for the music service"""
    for url in EXTRACTOR.find_urls(text):
        if \
            'open.spotify.com' in url or \
            'music.apple.com' in url:
            return url
        return None


def get_link(link: str) -> Optional[str]:
    """Get a global link from songlink"""
    result: str = None
    response = requests.get(
        url="https://api.song.link/v1-alpha.1/links",
        params={
            "url": link,
            "key": os.environ["SONGLINK_KEY"],
        },)
    if response.status_code == 200:
        result = response.json()['pageUrl']

    return result
