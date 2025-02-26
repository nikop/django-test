from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("past", views.past, name="past"),
    path("view/<int:id>", views.view, name="item"),
]
