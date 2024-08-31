import json
import logging.handlers
import os
import sys

from hydrogram import Client, filters
from hydrogram.enums import ParseMode

import config

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(asctime)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.handlers.TimedRotatingFileHandler(
            filename="apophis.log", when="midnight", backupCount=7
        ),
        logging.StreamHandler(stream=sys.stdout),
    ],
)
logging.getLogger("hydrogram").setLevel(logging.WARNING)


class Apophis(Client):
    logger = logging.getLogger("Apophis")

    def __init__(self):
        super().__init__(
            name="apophis",
            plugins={"root": "plugins"},
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            parse_mode=ParseMode.MARKDOWN,
            workers=10,
            in_memory=False
        )
        self.afk = False
        self.afk_cache = []
        self.afk_reason = config.AFK_REASON

        self.highlight_words = [word.lower() for word in config.HIGHLIGHT_WORDS]

    async def start(self: "Apophis"):
        await super().start()

        self.logger.info(f"Logged in > {self.me.full_name} ({self.me.id})")
        self.logger.info(f"Prefix > {config.PREFIX}")

    @staticmethod
    def cmd_filter(text: str | list[str]):
        if config.SECONDARY_ACCOUNT:
            return filters.command(text, config.PREFIX) & filters.user([config.CONTROLLED_BY_ID])
        return filters.command(text, config.PREFIX) & filters.me


if __name__ == "__main__":
    os.system(f"title Apophis Selfbot v1.00 - Prefix: {config.PREFIX}")
    if config.API_ID == 123 or len(config.API_HASH) < 8:
        print("You must fill out the config before running.")
        exit()
    bot = Apophis()
    bot.run()
