import discord
from config import DISCORD_BOT_TOKEN
from controller import QuestionController, BotController
from service.qa_service import QAService
import argparse


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

bot_controller = BotController(client)

parser = argparse.ArgumentParser()
parser.add_argument("--rebuild", action="store_true", help="Force rebuild of FAISS index.")
args = parser.parse_args()

qa_service = None
if args.rebuild:
    qa_service = QAService(True)
else:
    qa_service = QAService(False)
question_controller = QuestionController(client, qa_service)

client.run(DISCORD_BOT_TOKEN);