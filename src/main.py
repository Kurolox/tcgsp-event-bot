import discord
import os
import sqlalchemy
from dotenv import load_dotenv

# Use environment variables from .env file if available
load_dotenv()

# Initialize the database connection
database = sqlalchemy.create_engine("postgresql://" + os.getenv("EVENTBOT_DB_ENGINE"))

# Initialize the Discord bot client
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# Start the Discord bot
client.run(os.getenv("EVENTBOT_BOT_TOKEN"))