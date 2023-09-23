from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('add/', views.add, name='add'),
    # path('user_orders/', views.user_orders, name='user_orders')
]
