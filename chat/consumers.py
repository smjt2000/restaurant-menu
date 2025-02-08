import json
import datetime

from channels.generic.websocket import AsyncWebsocketConsumer


IRAN = datetime.timezone(datetime.timedelta(hours=3.5))

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.table_name = self.scope["url_route"]["kwargs"]["table_name"]
        self.table_group_name = "call_waiter"
        self.scope['session']['table_name'] = self.table_name
        self.scope['session'].asave()

        # Join room group
        await self.channel_layer.group_add(self.table_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.table_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        table_name = text_data_json["table_name"]
        now = datetime.datetime.now(IRAN)
        now = now.strftime("%H:%M:%S")

        # Send message to room group
        await self.channel_layer.group_send(
            self.table_group_name, {"type": "chat.message", "table_name": table_name, "time": now}
        )

    # Receive message from room group
    async def chat_message(self, event):
        table_name = event["table_name"]
        now = datetime.datetime.now(IRAN)
        now = now.strftime("%H:%M")

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"table_name": table_name, "time": now}))
