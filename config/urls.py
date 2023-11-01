from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("", views.home_teams),
    path("<team_name>", views.show_teams),
    path("<team_name>/members", views.show_members, name="show_members"),
]
