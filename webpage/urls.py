"""tbears URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('main/', views.first, name='main'),
    # path('main/list/', views.check, name='list'),
    # path('view/<int:num>', views.view, name='list'),
    path('Sample/', views.sample),
    # path('test/', views.Gameroom_list, name='game'),
    path('Ori/', views.Original),
    path('room/', views.room_list),
    path('make/', views.MakeGameRoom),
]
