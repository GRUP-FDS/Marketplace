from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import SignupForm

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def signup(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)

    if form.is_valid():
      user = form.save()

      login(request, user)

      return redirect('home')

  return render(request, 'core/signup.html')
