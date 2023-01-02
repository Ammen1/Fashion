from django.contrib import admin
from django.contrib import admin

from .models import Customer,User, Designer, Address,Manager

admin.site.register(Customer)
admin.site.register(User)
admin.site.register(Designer)
admin.site.register(Address)
admin.site.register(Manager)
