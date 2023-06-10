from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewCarForm, EditCarForm
from carros.models import Car
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib import messages
from carros.models import Car
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

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

@login_required
def edit(request, pk):
    car = get_object_or_404(Car, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditCarForm(request.POST, request.FILES, instance=car)

        if form.is_valid():
            form.save()

            return redirect('carros:pdp', pk=car.id)
    else:
        form = EditCarForm(instance=car)

    return render(request, 'carros/edit-form.html', {
        'form': form,
    })

def car_list(request):
    search = request.GET.get('search')
    #objects = Car.objects.filter(car_model__icontains=search)
    objects = Car.objects.filter(created_by=request.user, is_sold=False)  # Somente carros do usuário atual e não vendidos
    context = {'carros': objects}
    return render(request, 'carros/description.html', context)

def plp(request):
    search = request.GET.get('search')
    brand = request.GET.get('brand')

    # Filtros adicionais
    marca = request.GET.get('marca')
    modelo = request.GET.get('modelo')
    ano = request.GET.get('ano')
    cor = request.GET.get('cor')
    quilometragem = request.GET.get('quilometragem')
    combustivel = request.GET.get('combustivel')
    carroceria = request.GET.get('carroceria')
    preco = request.GET.get('preco')

    #cars = Car.objects.all()
    cars = Car.objects.filter(is_sold=False)  # Somente carros não vendidos

    if search:
        cars = cars.filter(car_model__icontains=search)
    if brand:
        cars = cars.filter(brand=brand)
    if marca:
        cars = cars.filter(brand__icontains=marca)
    if modelo:
        cars = cars.filter(car_model__icontains=modelo)
    if ano:
        cars = cars.filter(year=ano)
    if cor:
        cars = cars.filter(color__icontains=cor)
    if quilometragem:
        cars = cars.filter(mileage=quilometragem)
    if combustivel:
        cars = cars.filter(fuel_type__icontains=combustivel)
    if carroceria:
        cars = cars.filter(type__icontains=carroceria)
    if preco:
        cars = cars.filter(price=preco)

    context = {
        'cars': cars,
        'Marca': Car.objects.values_list('brand', flat=True).distinct(),
        'Modelo': Car.objects.values_list('car_model', flat=True).distinct(),
        'Ano': Car.objects.values_list('year', flat=True).distinct(),
        'Cor': Car.objects.values_list('color', flat=True).distinct(),
        'Quilometragem': Car.objects.values_list('mileage', flat=True).distinct(),
        'Combustível': Car.objects.values_list('fuel_type', flat=True).distinct(),
        'Tipo de Carroceria': Car.objects.values_list('type', flat=True).distinct(),
        'Preço': Car.objects.values_list('price', flat=True).distinct()
    }

    return render(request, 'carros/paginadelistagem.html', context)




def pdp(request, pk):
   car = get_object_or_404(Car, pk=pk)
  
   return render(request, 'carros/paginadedescricao.html', {
      'car': car
   }) 

def finalize(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if car.created_by == request.user:
        car.is_sold = True
        car.save()
        return HttpResponseRedirect(reverse('carros:pdp', args=[car_id]))
    else:
        # Adicione o tratamento para quando o usuário não for o criador do carro
        return redirect('home')  # Ou redirecione para outra página, se preferir

