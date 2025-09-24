class QuestionController:
    def __init__(self, client):
        self.client = client
        self.register_events()

    def register_events(self):
        # notifies the server when the bot is ready and active
        @self.client.event
        async def on_ready():
            print(f'We have logged in as {self.client.user}')

        # testing commands
        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return

            if message.content.startswith('$hello'):
                await message.channel.send('Hello!')

        # snitch method to prevent unseen message edits
        @self.client.event
        async def on_message_edit(before, after):
            if after.author == self.client.user:
                return
            
            if before.content != after.content:
                await after.channel.send("Hey! Your original message was: " + before.content, reference=before)