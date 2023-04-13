from django.shortcuts import render, redirect
from .forms import NewCarForm
from carros.models import Car

# Create your views here.
def new(request):
  if request.method == 'POST':
    form = NewCarForm(request.POST, request.FILES)

    if form.is_valid():
      item = form.save(commit=False)
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


def plp(request):
    search = request.GET.get('search')
    if search:
        cars = Car.objects.filter(car_model__icontains=search)
    else:
        cars = Car.objects.all()
    return render(request, 'carros/paginadelistagem.html', {'cars': cars})


def pdp(request):
   return render(request, 'carros/description.html', {
   }) 

