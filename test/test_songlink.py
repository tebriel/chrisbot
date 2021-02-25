"""Test Songlink Helpers"""

from chrisbot.songlink import extract_link


def test_extract_music_link():
    """Test that we can extract a music link"""
    url = 'https://open.spotify.com/track/4UJy3KwUdJ4NOitSqOqAce'
    text = f'some text {url} goes here'
    actual = extract_link(text)
    assert actual == url
