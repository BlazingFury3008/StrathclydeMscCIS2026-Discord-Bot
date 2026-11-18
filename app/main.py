"""
Discord Main App file
"""

import discord
from discord.ext import commands

from app.helper.logging import logging_handler, main_logger
from app.helper.config import DISCORD_TOKEN
from app.cogs.example import ExampleCog


# Discord Bot Intents
intents = discord.Intents.default()

intents.message_content = True
intents.members = True


# Discord Bot Configuration
class DiscordBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents
        )

    async def setup_hook(self):
        # Register Cogs
        await self.add_cog(ExampleCog(self))

        # Synchronise slash commands (This needs to be done)
        synced = await self.tree.sync()

        main_logger.info(
            f"Synchronised {len(synced)} application commands"
        )

# Instead of using discord.Client, as we need to sync commands
client = DiscordBot()

# Start Discord Bot
client.run(DISCORD_TOKEN, log_handler=logging_handler)