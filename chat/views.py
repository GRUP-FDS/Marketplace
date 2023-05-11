from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from carros.models import Car
from .models import Chat, Message

# Create your views here.
def chat(request, id):
  buyerUsername = request.GET.get('buyer')

  car = Car.objects.get(pk=id)
  buyer = User.objects.get(username=buyerUsername)
  user = request.user
  creator_of_product = car.created_by

  messages = None
  chat = None

  try:
    chat = Chat.objects.get(car=car, seller=creator_of_product, buyer=buyer)

    messages = Message.objects.filter(chat=chat)
  except ObjectDoesNotExist:
    chat = Chat(buyer=user, seller=car.created_by, car=car)
    chat.save()

  return render(request, 'chat/index.html', {
    'car': car,
    'chat': chat,
    'messages': messages
  })