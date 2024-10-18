from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Shopping_car/', views.Shopping_car, name='Shopping_car'),
    path('checkout/',views.checkout, name='/checkout'),
]