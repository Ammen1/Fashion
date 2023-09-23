from django.db import models
from django.utils.translation import gettext_lazy as _


class DeliveryOptions(models.Model):
    """
    The Delivery methods table contining all delivery
    """

    DELIVERY_CHOICES = [
        ("IS", "In Store"),
        ("HD", "Home Delivery"),
        ("DD", "Digital Delivery"),
    ]

    delivery_name = models.CharField(
        verbose_name=_("delivery_name"),
        help_text=_("Required"),
        max_length=255,
    )
    delivery_price = models.DecimalField(
        verbose_name=_("delivery price"),
        help_text=_("Maximum 99999999999999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 99999999999999.99."),
            },
        },
        max_digits=14,
        decimal_places=2,
    )
    delivery_method = models.CharField(
        choices=DELIVERY_CHOICES,
        verbose_name=_("delivery_method"),
        help_text=_("Required"),
        max_length=255,
    )
    delivery_timeframe = models.CharField(
        verbose_name=_("delivery timeframe"),
        help_text=_("Required"),
        max_length=255,
    )
    delivery_window = models.CharField(
        verbose_name=_("delivery window"),
        help_text=_("Required"),
        max_length=255,
    )
    order = models.IntegerField(verbose_name=_("list order"), help_text=_("Required"), default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Delivery Option")
        verbose_name_plural = _("Delivery Options")

    def __str__(self):
        return self.delivery_name


class PaymentSelections(models.Model):
    """
    Store payment options
    """

    name = models.CharField(
        verbose_name=_("name"),
        help_text=_("Required"),
        max_length=255,
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Payment Selection")
        verbose_name_plural = _("Payment Selections")

    def __str__(self):
        return self.name

from django.db import models
from uuid import uuid4


class ChapaStatus(models.TextChoices):
    PENDING = 'pending', 'PENDING'
    SUCCESS = 'success', 'SUCCESS'
    CREATED = 'created', 'CREATED'
    FAILED = 'failed', 'FAILED'


class ChapaTransactionMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)

    amount = models.FloatField()
    currency = models.CharField(max_length=25, default='ETB')
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    event = models.CharField(max_length=255, null=True, blank=True)

    status = models.CharField(max_length=50, choices=ChapaStatus.choices, default=ChapaStatus.CREATED)

    response_dump = models.JSONField(default=dict)  # incase the response is valuable in the future

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.first_name} - {self.last_name} | {self.amount}"
    
    def serialize(self) -> dict:
        return {
            'amount': self.amount,
            'currency': self.currency,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'description': self.description
        }

# TODO: add non abstract model


class ChapaTransaction(ChapaTransactionMixin):
    pass
