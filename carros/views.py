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
    ##objects = Car.objects.filter(search)
    print(search)
    ##context = {'carros': objects}
    ##print(context)
    return render(request, 'carros/description.html')

def plp(request):
    cars = Car.objects.all()
    search = request.GET.get('search')
    
    return render(request, 'carros/paginadelistagem.html',{
        'cars' : cars,
    })

def pdp(request):
   return render(request, 'carros/description.html', {
   }) 

