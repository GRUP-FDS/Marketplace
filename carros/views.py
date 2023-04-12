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
    template_name = 'produto_list.html'
    objects = Car.objects.all()
    search = request.GET.get('search')
    print({'search': search})
    if search:
        objects = objects.filter(produto__icontains=search)
    context = {'object_list': objects}
    return render(request, template_name, context)

def plp(request):
    cars = Car.objects.all()
    search = request.GET.get('search')
    
    return render(request, 'carros/paginadelistagem.html',{
        'cars' : cars,
    })

def pdp(request):
   return render(request, 'carros/description.html', {
   }) 

