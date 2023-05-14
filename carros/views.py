from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewCarForm
from carros.models import Car
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib import messages
from carros.models import Car

# Create your views here.
def new(request):
  if request.method == 'POST':
    form = NewCarForm(request.POST, request.FILES)

    if form.is_valid():
      item = form.save(commit=False)
      item.created_by = request.user
      item.save()

      return redirect('home')
  else:
    form = NewCarForm()

  return render(request, 'carros/form.html', {
    'form': form,
    'title': 'Novo Anúncio'
  })

def car_list(request):
    search = request.GET.get('search')
    objects = Car.objects.filter(car_model__icontains=search)
    context = {'carros': objects}
    return render(request, 'carros/description.html', context)

def car_filter(request):
    queryset = Car.objects.all()
    
    if 'marca' in request.GET:
        marca = request.GET['marca']
        if marca:
            queryset = queryset.filter(make__icontains=marca)
    
    if 'modelo' in request.GET:
        modelo = request.GET['modelo']
        if modelo:
            queryset = queryset.filter(model__icontains=modelo)
    
    if 'ano' in request.GET:
        ano = request.GET['ano']
        if ano:
            queryset = queryset.filter(year=ano)
    
    if 'cor' in request.GET:
        cor = request.GET['cor']
        if cor:
            queryset = queryset.filter(color__icontains=cor)
    
    if 'quilometragem' in request.GET:
        quilometragem = request.GET['quilometragem']
        if quilometragem:
            queryset = queryset.filter(mileage=quilometragem)
    
    if 'combustivel' in request.GET:
        combustivel = request.GET['combustivel']
        if combustivel:
            queryset = queryset.filter(fuel_type__icontains=combustivel)
    
    if 'carroceria' in request.GET:
        carroceria = request.GET['carroceria']
        if carroceria:
            queryset = queryset.filter(type__icontains=carroceria)
    
    if 'preco' in request.GET:
        preco = request.GET['preco']
        if preco:
            queryset = queryset.filter(price=preco)
    
    brand = queryset.values_list('make', flat=True).distinct()
    car_model = queryset.values_list('model', flat=True).distinct()
    year = queryset.values_list('year', flat=True).distinct()
    mileage = queryset.values_list('mileage', flat=True).distinct()
    fuel_type = queryset.values_list('fuel_type', flat=True).distinct()
    car_type = queryset.values_list('type', flat=True).distinct()
    price = queryset.values_list('price', flat=True).distinct()
    color = queryset.values_list('color', flat=True).distinct()
    
    context = {
        'Marca': brand,
        'Modelo': car_model,
        'Ano': year,
        'Cor': color,
        'Quilometragem': mileage,
        'Combustível': fuel_type,
        'Tipo de Carroceria' : car_type,
        'Preço' : price
    }
    
    return render(request, 'paginalistagem.html', context)


def plp(request):
    search = request.GET.get('search')
    brand = request.GET.get('brand')

    if search:
        cars = Car.objects.filter(car_model__icontains=search)
    else:
        cars = Car.objects.all()
    return render(request, 'carros/paginadelistagem.html', {'cars': cars})

def pdp(request, pk):
   car = get_object_or_404(Car, pk=pk)
  
   return render(request, 'carros/paginadedescricao.html', {
      'car': car
   }) 


