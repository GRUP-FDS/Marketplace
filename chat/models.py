from django.db import models

from django.contrib.auth.models import User
from carros.models import Car

# Create your models here.
class Chat(models.Model):
  buyer = models.ForeignKey(User, related_name="buyer_chats", on_delete=models.CASCADE)
  seller = models.ForeignKey(User, related_name="seller_chats", on_delete=models.CASCADE)
  car = models.ForeignKey(Car, related_name="car_chats", on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return 'Comprador: ' + self.buyer.username + ' - Vendedor: ' + self.seller.username
  
class Message(models.Model):
  chat = models.ForeignKey(Chat, related_name="messages", on_delete=models.CASCADE)
  user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
  content = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('date_added',)

  def __str__(self):
    return self.content