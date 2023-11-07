from django.urls import path

from . import views

urlpatterns = [
    path("", views.decodeUserMessage, name="decode"),
]
