# This example requires the 'message_content' intent.

import discord
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# notifies the server when the bot is ready and active
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# testing commands
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# snitch method to prevent unseen message edits
@client.event
async def on_message_edit(before, after):
    if after.author == client.user:
        return
    
    if before.content != after.content:
        await after.channel.send("Hey! Your original message was: " + before.content, reference=before)


client.run(DISCORD_BOT_TOKEN);
