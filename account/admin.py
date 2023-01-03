from django.contrib import admin


from .models import User, Designer, Manager


admin.site.register(User)
admin.site.register(Designer)

admin.site.register(Manager)
