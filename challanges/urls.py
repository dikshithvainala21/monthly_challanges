from . import views
from django.urls import path



urlpatterns = [
  path("January",views.index),
  path("February",views.february)
]