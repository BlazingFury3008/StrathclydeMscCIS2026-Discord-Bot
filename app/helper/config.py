from dotenv import load_dotenv
import os

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if DISCORD_TOKEN == "":
    raise ValueError("DISCORD_TOKEN Enviroment Variable needs set")

LOGGING_DIRECTORY = os.getenv("LOGGING_DIRECTORY")

if LOGGING_DIRECTORY == "":
    raise ValueError("LOGGING_DIRECTORY Enviroment Variable needs set")