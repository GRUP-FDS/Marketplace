from django import forms
from .models import Car

INPUT_CLASSES = 'w-full mt-2 px-4 py-2 rounded-xl border border-2 border-gray-400'

class NewCarForm(forms.ModelForm):
  class Meta:
    model = Car
    fields = ('brand', 'car_model', 'mileage', 'year', 'fuel_type', 'type', 'price', 'color', 
              'image', 'description')
    labels = {
      'brand': 'Marca',
      'car_model':'Modelo',
      'year':'Ano',
      'mileage': 'Quilometragem', 
      'fuel_type':'Tipo de Combustível', 
      'type': 'Estado do Veículo',
      'price': 'Preço',
      'color':'Cor',
      'description': 'Descrição',
      'image': 'Imagem',
    }

    widgets = {
      'brand': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'car_model': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'year': forms.NumberInput(attrs={
        'class': INPUT_CLASSES
      }),
      'mileage': forms.NumberInput(attrs={
        'class': INPUT_CLASSES
      }),
      'type': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'fuel_type': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'price': forms.NumberInput(attrs={
        'class': INPUT_CLASSES
      }),
      'color': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'description': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'image': forms.FileInput(attrs={
        'class': INPUT_CLASSES
      }),
    }
  
class EditCarForm(forms.ModelForm):
  class Meta:
    model = Car
    fields = ('brand', 'car_model', 'mileage', 'year', 'fuel_type', 'type', 'price', 'color', 'image', 'description')
    labels = {
      'brand': 'Marca',
      'car_model':'Modelo',
      'year':'Ano',
      'mileage': 'Quilometragem', 
      'fuel_type':'Tipo de Combustível', 
      'type': 'Estado do Veículo',
      'price': 'Preço',
      'color':'Cor',
      'description': 'Descrição',
      'image': 'Imagem',
    }

    widgets = {
      'brand': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'car_model': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'year': forms.NumberInput(attrs={
        'class': INPUT_CLASSES
      }),
      'mileage': forms.NumberInput(attrs={
        'class': INPUT_CLASSES
      }),
      'type': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'fuel_type': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'price': forms.NumberInput(attrs={
        'class': INPUT_CLASSES
      }),
      'color': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'description': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'image': forms.FileInput(attrs={
        'class': INPUT_CLASSES
      }),
    }

