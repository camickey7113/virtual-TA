import discord
from service import QAService

class QuestionController:
    def __init__(self, client):
        self.client = client
        self.register_events()

    def register_events(self):
        # testing commands
        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return
            
            if message.channel.type == discord.ChannelType.public_thread:
                parent = message.channel.parent
                if parent and parent.type == discord.ChannelType.forum and message.id == message.channel.id:
                    response = QAService.question_to_answer(message.content)
                    await message.channel.send(response)

            # response = QAService.question_to_answer(message.content)
            # await message.channel.send(response)

            