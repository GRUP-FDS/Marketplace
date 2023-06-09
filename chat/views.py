from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from carros.models import Car
from .models import Chat, Message

# Create your views here.
def chat(request, id):
  buyerUsername = request.GET.get('buyer')
  sellerUsername = request.GET.get('seller')

  car = Car.objects.get(pk=id)
  buyer = User.objects.get(username=buyerUsername)
  user = request.user
  creator_of_car = car.created_by

  messages = None
  chat = None


  try:
    chat = Chat.objects.get(car=car, seller=creator_of_car, buyer=buyer)

    messages = Message.objects.filter(chat=chat)
  except ObjectDoesNotExist:
    chat = Chat(buyer=user, seller=car.created_by, car=car)
    chat.save()

  print(messages)
  return render(request, 'chat/index.html', {
    'car': car,
    'chat': chat,
    'messages': messages
  })

