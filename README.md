# ChrisBot

ChrisBot is a [Keybase](https://keybase.io) bot.

## Problems

- Uses paper key instead of bot token
- Must include `/home/keybase/.config` directory because of Device Registration requirements
- Python library doesn't enable bot token or bot API calls (like advertising commands)
- Python library (much like Keybase itself) is unmaintained
- Incompatible with Python 3.9+

## Features

- Uses the [song.link](https://song.link) API to convert an apple music or spotify share URL into a universal
  URL (when possible).
