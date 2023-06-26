from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name='login'),
    path('home/', views.HOME, name= 'home'),
    path('register/', views.Register, name='register'),
    path('showproduct/',views.ShowProduct, name="showproduct"),
]