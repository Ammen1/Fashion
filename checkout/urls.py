from django.urls import  path

from . import views

app_name = "checkout"

urlpatterns = [
    path("deliverychoices", views.deliverychoices, name="deliverychoices"),
    path("basket_update_delivery/", views.basket_update_delivery, name="basket_update_delivery"),
    path("delivery_address/", views.delivery_address, name="delivery_address"),
    path("payment_selection/", views.payment_selection, name="payment_selection"),
    path("payment_complete/", views.payment_complete, name="payment_complete"),
    path("payment_successful/", views.payment_successful, name="payment_successful"),
    path("pay_chapa/", views.pay_chapa, name="pay_chapa"),
    path('chapa_view/', views.chapa_view, name='chapa_view'),
    # path('webhook/', views.chapa_webhook, name='chapa_webhook'),
    # ...


 ]
