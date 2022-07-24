import discord

from discord.ext import commands
from pathlib import Path
from os import getenv
from dotenv import load_dotenv

from schemas.base import create_tables


# Use environment variables from .env file if available
load_dotenv()

# Initialize the Discord bot client, defining all needed intents and import all defined cogs
# https://docs.pycord.dev/en/master/intents.html
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), guild_ids=[992765224459452428])

# Load all the defined cogs
for cog in [node for node in (Path(__file__).resolve().parent / "cogs").iterdir() if node.is_file()]:
        bot.load_extension(f"cogs.{cog.stem}")

create_tables()
# Start the Discord bot
print("Bot initialization complete. Deploying bot...")
bot.run(getenv("EVENTBOT_BOT_TOKEN"))