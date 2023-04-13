from django.urls import path
from .views import car_list
from . import views

urlpatterns = [
    path('new/', views.new, name="new"),
    path('pdp/', views.pdp, name="pdp"),
    path('plp/', views.plp, name="plp"),
    path('car_list/', views.car_list, name="car_list")
]