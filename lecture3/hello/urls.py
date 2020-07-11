from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("aa", views.aadil, name="Aadil"),
    path("<str:name>", views.greet, name="greet")
]