class BotController:
    def __init__(self, client):
        self.client = client
        self.register_events()

    def register_events(self):
        # notifies the server when the bot is ready and active
        @self.client.event
        async def on_ready():
            print(f'We have logged in as {self.client.user}')