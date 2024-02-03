from django.urls import path
from app import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name="home"),
]
