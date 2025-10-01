import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

EMBEDDING_MODEL = "text-embedding-3-small"
FAISS_INDEX_PATH = "faiss_index"