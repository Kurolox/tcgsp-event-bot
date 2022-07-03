import sqlalchemy
import discord

from discord.ext import commands
from pathlib import Path
from os import getenv
from dotenv import load_dotenv

from schemas.base import Base

# Use environment variables from .env file if available
load_dotenv()

# Initialize the database connection
database = sqlalchemy.create_engine(getenv("EVENTBOT_DB_ENGINE"))
Base.metadata.create_all(database, checkfirst=True)
session = sqlalchemy.orm.sessionmaker(bind=database)()

# Initialize the Discord bot client, defining all needed intents and import all defined cogs
# https://docs.pycord.dev/en/master/intents.html
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

for cog in [node for node in (Path(__file__).resolve().parent / "cogs").iterdir() if node.is_file()]:
        bot.load_extension(f"cogs.{cog.stem}")

@bot.command()
async def command(ctx):
        print("commanded")

# Start the Discord bot
print("Bot initialization complete. Deploying bot...")
bot.run(getenv("EVENTBOT_BOT_TOKEN"))