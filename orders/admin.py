from django.contrib import admin

from .models import Order, OrderItem


admin.site.register(OrderItem)

class orderAdmin(admin.ModelAdmin):
    list_display= ('full_name','email','address1', 'address2', 'phone', 'postal_code','country_code', 'total_paid', 'billing_status')
    list_per_page= 10

admin.site.register(Order,orderAdmin)    