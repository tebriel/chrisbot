"""Main ChrisBot Entry Point"""
import asyncio
import logging
import os
import signal
import sys

from pykeybasebot import Bot, Source, KbEvent
import pykeybasebot.types.chat1 as chat1
from chrisbot import songlink

logging.basicConfig(level=logging.DEBUG)

BOT_LOOP = None
BOT_USERNAME = os.environ["KEYBASE_USERNAME"]

def handler(signum, _):
    """Handle stop event"""
    print('Received Signal', signum)
    if BOT_LOOP is not None:
        BOT_LOOP.close()
    sys.exit(0)

signal.signal(signal.SIGTERM, handler)


class Handler:
    """Handles incoming messages from keybase"""
    async def __call__(self, bot, event) -> None:
        if self.should_skip(event):
            return

        message = event.msg.content.text.body

        media_url = songlink.extract_link(message)
        if media_url:
            new_url = songlink.get_link(media_url)
            if new_url is None:
                return
            channel = event.msg.channel
            await bot.chat.send(channel, new_url)
            return

        if event.msg.content.text.body == "ping🌴":
            channel = event.msg.channel
            await bot.chat.send(channel, "🍹PONG!🍹")
        else:
            print(event)

    @staticmethod
    def should_skip(event: KbEvent) -> bool:
        """Determine if we should skip this message"""
        if event.msg.content.type_name != chat1.MessageTypeStrings.TEXT.value:
            return True
        # Avoid duplicates when local + remote come through
        if event.source != Source.REMOTE:
            return True
        # This is bad, we should use the UUID
        # if event.msg.sender.username == BOT_USERNAME:
        #     return True
        return False


listen_options = {
    "local": True,
    "wallet": True,
    "dev": True,
    "hide-exploding": False,
    "convs": True,
    "filter_channel": None,
    "filter_channels": None,
}

chrisbot = Bot(
    username=BOT_USERNAME,
    paperkey=os.environ.get("KEYBASE_PAPERKEY"),
    handler=Handler(),
)


if __name__ == '__main__':
    print('hello, world!')
    loop = asyncio.run(chrisbot.start(listen_options))
