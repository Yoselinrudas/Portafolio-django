from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.iniciar, name='richard'),
    path('insertar/', views.insertar, name='insertar'),
    path('login/', views.login, name='login'),
    path('portafoleo/', views.portafoleo, name='portafoleo'),
]


