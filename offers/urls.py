from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.offer_list, name="offer_list"),
    path('electronics', views.electronics_list, name="electronics_list"),
    path('hygiene', views.hygiene_list, name="hygiene_list"),
    path('clothes', views.clothes_list, name="clothes_list"),
    path('sports', views.sports_list, name="sports_list"),
]
