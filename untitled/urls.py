"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from first_app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create_poll/', views.create_poll, name="create_poll"),
    path('get_poll/', views.get_poll, name="get_poll"),
    path('delete_poll/', views.delete_poll, name="delete_poll"),
    path('add_vote/', views.add_vote, name="add_vote"),
    path('get_rooms/', views.get_rooms, name="get_rooms"),
    path('get_all_polls/', views.get_all_polls, name="get_all_polls"),
    path('email/', views.email, name="email"),
    path('reserve_room/', views.reserve_room, name="reserve_room"),
    path('get_meeting/', views.get_meeting, name="get_meeting"),
    path('get_all_meetings/',views.get_all_meetings, name="get_all_meetings"),
    path('admin/', admin.site.urls),
]
