from django.urls import path
from . import views
from django.contrib import admin

app_name = 'myapp'
urlpatterns = [
    path('homework',views.homework),
    path('index',views.index),
    path('recommend',views.recommend),
    path('fact',views.fact),
]