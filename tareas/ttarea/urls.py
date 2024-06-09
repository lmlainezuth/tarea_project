from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('tareas/', views.lista_tareas, name='lista_tareas'),
]
