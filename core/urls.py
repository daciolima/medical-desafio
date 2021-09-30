from django.contrib import admin
from django.urls import path

from .views import HomeView, UmlView

app_name = "core"

urlpatterns = [
    path('', HomeView.as_view(), name="index"),
    path('projeto', UmlView.as_view(), name="uml")
]