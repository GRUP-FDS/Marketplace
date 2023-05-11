from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewCarForm
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

