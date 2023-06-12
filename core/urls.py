from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('my-ads/', views.my_ads, name="my_ads"),
    path('chats/', views.my_chats, name="my_chats"),
    path('my-ads/delete/<int:pk>/', views.delete_ad, name='delete_car'),
]