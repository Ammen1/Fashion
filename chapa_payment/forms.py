from django import forms
from chapa_payment.models import ChapaTransaction


class ChapaWebhookForm(forms.ModelForm):
    class Meta:
        model = ChapaTransaction
        fields = ('email', 'amount', 'currency', 'first_name', 'last_name', 'description')
