import discord
from config import DISCORD_BOT_TOKEN
from controller import QuestionController

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

question_controller = QuestionController(client)

client.run(DISCORD_BOT_TOKEN);
