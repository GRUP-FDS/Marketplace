from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse

from .forms import SignupForm

# Create your views here.
def home(request):
  if request.method == 'POST':
    search = request.POST.get('search')

    return redirect(reverse('carros:plp') + '?search=' + search)
  else:
    return render(request, 'core/home.html')

def signup(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)

    if form.is_valid():
      user = form.save()

      login(request, user)

      return redirect('home')

  return render(request, 'core/signup.html')
