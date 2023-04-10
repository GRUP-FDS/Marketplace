from django.shortcuts import render, redirect

# Create your views here.
def new(request):
  return render(request, 'carros/form.html', {
    'title': 'Novo anúncio'
  })