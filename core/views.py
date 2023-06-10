from carros.models import Car
from chat.models import Chat
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import SignupForm


# Create your views here.
def home(request):
  if request.method == 'POST':
    search = request.POST.get('search')

    return redirect(reverse('carros:plp') + '?search=' + search)
  else:
    return render(request, 'core/home.html')

def my_ads(request):
    cars = Car.objects.filter(created_by=request.user)
    return render(request, 'core/my_ads.html', {'cars': cars})

@login_required
def delete_ad(request, pk):
    car = get_object_or_404(Car, pk=pk, created_by=request.user)
    try:
        car.delete()
        messages.success(request, 'Anúncio deletado com sucesso.')
    except:
        messages.error(request, 'Ocorreu um erro ao deletar o anúncio.')
    return redirect('my_ads')


def signup(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)

    if form.is_valid():
      user = form.save()

      login(request, user)

      return redirect('home')
  else:
      form = SignupForm()

  return render(request, 'core/signup.html', {'form': form})

@login_required
def my_chats(request):
  chats = Chat.objects.filter(Q(buyer=request.user) | Q(seller=request.user))

  return render(request, 'core/chats.html', {
     'chats': chats
  })