from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.apps import apps
from chapa_payment.forms import ChapaWebhookForm
import json


@csrf_exempt
def chapa_webhook(request):
    if request.method != 'POST':
        return JsonResponse(
            {
                'errors': 'Only POST method allowed'
            },
            status=400,
        )

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse(
            {
                'error': "Invalid JSON body"
            },
            status=400
        )

    model_path = getattr(settings, 'CHAPA_TRANSACTION_MODEL', '')
    if not model_path:
        return JsonResponse(
            {
                'error': 'CHAPA_TRANSACTION_MODEL setting not defined'
            },
            status=500,
        )

    model = apps.get_model(model_path)
    if model is None:
        return JsonResponse(
            {
                'error': f"Model '{model_path}' not found"
            },
            status=500,
        )

    form = ChapaWebhookForm(data)
    if not form.is_valid():
        return JsonResponse(
            {
                'error': 'Invalid data'
            },
            status=400
        )

    instance = form.save()

    return JsonResponse(
        {
            'success': True,
            'instance_id': instance.pk
        }
    )
