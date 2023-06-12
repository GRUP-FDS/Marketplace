from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect

from carros.models import Car
from .models import Chat, Message

# Create your views here.
def chat(request, id):
  if request.method == 'POST':
    message = request.POST.get('content')
    buyerUsername = request.POST.get('user')
    chatId = request.POST.get('chat')

    chat = Chat.objects.get(id=int(chatId))
    userBuyer = User.objects.get(username=buyerUsername)

    Message.objects.create(user=userBuyer, content=message, chat=chat)

    return redirect(request.META['HTTP_REFERER'])

  else:
    buyerUsername = request.GET.get('buyer')

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

  return render(request, 'chat/index.html', {
    'car': car,
    'chat': chat,
    'messages': messages
  })
