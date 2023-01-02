
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("prodect.urls", namespace="prodect")), #, namespace="prodect"
    path("checkout/", include("checkout.urls", namespace="checkout")),#, namespace="checkout"
    path("basket/", include("basket.urls", namespace="basket")),#, namespace="basket"
    path("account/", include("account.urls", namespace="account")),#, namespace="account"
    path("orders/", include("orders.urls", namespace="orders")),#, namespace="orders"
    path("customer/",include("customer.urls", namespace="customer")),#, namespace="customer"
    path("promotion/", include("promotion.urls", namespace="promotion"))#, namespace="promotion"

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

