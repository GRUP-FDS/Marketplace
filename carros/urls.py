from django.urls import path

from . import views

urlpatterns = [
    path('new/', views.new, name="new"),
    path('pdp/', views.pdp, name="pdp"),
    path('plp/', views.plp, name="plp")
]