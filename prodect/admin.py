from django.contrib import admin

from . import models

admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.ProductType)
admin.site.register(models.ProductAttributeValue)
admin.site.register(models.Media)
admin.site.register(models.Stock)
admin.site.register(models.ProductAttributeValues)
admin.site.register(models.ProductTypeAttribute)



class InventoryAdmin(admin.ModelAdmin):
    list_display = ("product", "store_price")


admin.site.register(models.ProductInventory, InventoryAdmin)
