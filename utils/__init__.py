from utils.logger import setup_logger
from discord.ext import commands
from discord import Intents
import json

with open('config.json') as config_file:
    config = json.load(config_file)

logger = setup_logger()
intents = Intents.default()
intents.message_content = True

class DiscordBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix=commands.when_mentioned_or(config["prefix"]),
            intents=intents,
            help_command=None,
        )
        self.logger = logger