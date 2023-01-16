from django.contrib import admin

from . import models

admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.ProductType)

admin.site.register(models.ProductSpecification)
admin.site.register(models.ProductSpecificationValue)
admin.site.register(models.ProductImage)




class InventoryAdmin(admin.ModelAdmin):
    list_display = ("product", "store_price")


# admin.site.register(models.ProductInventory, InventoryAdmin)

