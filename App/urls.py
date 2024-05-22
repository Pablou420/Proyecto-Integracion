from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('entrantes/', views.entrantes, name='entrantes'),
    path('platos/', views.platos, name='platos'),
    path('postres/', views.postres, name='postres'),
    path('acompañantes/', views.acompañantes, name='acompañantes'),
    path('carrito/', views.carrito, name='carrito'),
]