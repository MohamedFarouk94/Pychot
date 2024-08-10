import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from database.models import ChatRoom, Message


class EchoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        await self.send(text_data=json.dumps({
            'message': text_data
        }))


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('@' * 100)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        if not self.scope["user"].is_authenticated:
            await self.close()
            return

        if not await self.user_in_room(self.scope["user"], self.room_name):
            await self.close()
            return

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        username = self.scope["user"].username

        await self.save_message(username, text_data)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': text_data,
                'username': username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    @database_sync_to_async
    def save_message(self, username, message):
        user = User.objects.get(username=username)
        room, created = ChatRoom.objects.get_or_create(name=self.room_name)
        return Message.objects.create(user=user, room=room, content=message)

    @database_sync_to_async
    def user_in_room(self, user, room_name):
        try:
            room = ChatRoom.objects.get(name=room_name)
            return room.participants.filter(id=user.id).exists()
        except ChatRoom.DoesNotExist:
            return False
