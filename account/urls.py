from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path('route', views.route, name="route"),
    path('map', views.map, name="map"),
    path("", views.account_register, name="register"),
]