"""
This is an example cog that can be used as a base for other cogs
It contains sample commands and events that can be used as a reference
"""

import discord
from discord.ext import commands
from discord import app_commands

from app.helper.logging import main_logger
from time import sleep

class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        """
        This event is called when the bot is ready to start recieving events and commands
        There are a few different events, which can be found here - https://discordpy.readthedocs.io/en/latest/api.html?highlight=on_ready#event-reference
        """
        main_logger.info(f"{self.bot.user} has connected to Discord")
        
    
    @app_commands.command(name="example", description="This is an example command")
    async def example_command(self, interaction: discord.Interaction):
        """
        This is a simple example command that responses with a message when called
        """
        main_logger.info(f"Recieved Example Command from {interaction.user}")
        await interaction.response.send_message("This is an example command response")
        
        
    @app_commands.command(name="delayed_example", description="This is an example command that responds after a delay")
    async def delayed_example_command(self, interaction: discord.Interaction):
        """
        This is an example delayed example command that responds after 5 seconds
        In most cases, you won't have a set delay, but if you have a program that can take a while to run,
        you can use this to
        1. Let the user know that the command is being processsed
        2. Prevent discord from timing out the command if it takes too long
        """
        main_logger.info(f"Recieved Example Delayed Command from {interaction.user}")
        await interaction.response.defer()
        sleep(3) # Simulating a long running process, such as a database query or API call etc
        main_logger.info(f"Finished processing Example Delayed Command from {interaction.user}")
        await interaction.followup.send("This is an example command that responds after a delay")
        
    @app_commands.command(name="input_example", description="This is an example command that takes an input")
    @app_commands.describe(input="This is an example input") # This is used to tell the user what the input parameter is
    async def input_example_command(self, interaction: discord.Interaction, input: str):
        """This is an example of a command that takes an input from a user

        Args:
            interaction (discord.Interaction): _description_
            input (str): _description_
        """
        
        main_logger.info(f"Recieved Example Input Command from {interaction.user} with input: {input}")
        await interaction.response.send_message(f"{interaction.user}, You said {input}")
    
