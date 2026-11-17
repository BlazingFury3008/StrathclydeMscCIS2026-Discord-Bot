"""
Discord Main App file
"""

import discord
from .helper.logging import logging_handler, main_logger
from .helper.config import DISCORD_TOKEN

# Discord Bot Intents
intents = discord.Intents.default()

intents.message_content = True
intents.members = True

# Discord  bot configurations
client = discord.Client(intents=intents)

# This runs when the bot connects
@client.event
async def on_ready():
    main_logger.info(f"{client.user} Has connected to Discord")
    
# This registers any time a message is sent
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    main_logger.info(f"Recieved Message from {message.author}")
    await message.channel.send(f"Hello - {message.author}")



client.run(DISCORD_TOKEN, log_handler=logging_handler)