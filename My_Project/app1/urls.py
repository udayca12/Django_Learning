from django.urls import path
from . import views

urlpatterns = [
    path('', views.play, name = 'play'), #localhost: 80000/app1
]
