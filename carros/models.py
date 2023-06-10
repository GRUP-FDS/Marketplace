from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
  car_model = models.CharField(max_length=255)
  brand = models.CharField(max_length=255)
  year = models.IntegerField()
  mileage=models.IntegerField()
  fuel_type=models.CharField(max_length=2551)
  type = models.CharField(max_length=255)
  price = models.FloatField()
  color = models.CharField(max_length=255)
  image = models.ImageField(upload_to='car_images', blank=True, null=True, default='imagem-padrao.jpeg')
  created_by = models.ForeignKey(User, related_name='cars', on_delete=models.CASCADE)
  description = models.TextField(blank=True, null=True)
  is_sold = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)



  def __str__(self):
    return self.car_model