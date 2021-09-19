from django.urls import path
from . import views
from django.contrib import admin

app_name = 'myapp'
urlpatterns = [
    path('ajax', views.ajax),
    path('more', views.more),
]