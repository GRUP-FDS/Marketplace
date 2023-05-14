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
    brand = Car.objects.values_list('make', flat=True).distinct()
    car_model = Car.objects.values_list('model', flat=True).distinct()
    year = Car.objects.values_list('year', flat=True).distinct()
    mileage = Car.objects.values_list('mileage', flat=True).distinct()
    fuel_type = Car.objects.values_list('fuel_type', flat=True).distinct()
    type = Car.objects.values_list('type', flat=True).distinct()
    price = Car.objects.values_list('price', flat=True).distinct()
    color = Car.objects.values_list('color', flat=True).distinct()
    
    context = {
        'Marca': brand,
        'Modelo': car_model,
        'Ano': year,
        'Cor': color,
        'Quilometragem': mileage,
        'Combustível': fuel_type,
        'Tipo de Carroceria' : type,
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


