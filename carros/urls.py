from django.urls import path
from . import views

app_name = 'carros'

urlpatterns = [
    path('new/', views.new, name="new"),
    path('<int:pk>/', views.pdp, name="pdp"),
    path('plp/', views.plp, name="plp"),  
]