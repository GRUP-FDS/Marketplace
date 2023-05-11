import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from django.contrib.auth.models import User

from .models import Chat, Message

class ChatConsumer(AsyncWebsocketConsumer):
  async def connect(self):
    self.chat_id = self.scope['url_route']['kwargs']['chat_id']
    self.chat_group_id = 'chat_%s' % self.chat_id

    await self.channel_layer.group_add(
      self.chat_group_id,
      self.channel_name
    )

    await self.accept()

  async def disconnect(self, code):
    await self.channel_layer.group_discard(
      self.chat_group_id,
      self.channel_name
    )
  
  async def receive(self, text_data):
    data = json.loads(text_data)

    message = data['message']
    chatId = data['chatId']
    buyer = data['buyer']

    await self.save_message(message, buyer, chatId)

    await self.channel_layer.group_send(
      self.chat_group_id,
      {
        'type': 'chat_message',
        'message': message,
        'buyer': buyer,
        'chatId': chatId
      }
    )

  async def chat_message(self, event):
    message = event['message']
    buyer = event['buyer']
    chatId = event['chatId'] 

    await self.send(text_data=json.dumps({
      'message': message,
      'buyer': buyer,
      'chatId': chatId
    }))

  @sync_to_async
  def save_message(self, message, buyer, chatId):
    chat = Chat.objects.get(id=chatId)
    userBuyer = User.objects.get(username=buyer)

    Message.objects.create(user=userBuyer, content=message, chat=chat)