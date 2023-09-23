from django.urls import path

from . import views

app_name = "chapa_payment"

urlpatterns = [
    path('', views.chapa_webhook, name="chapa_webhook"),

]
