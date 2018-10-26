from datetime import datetime, timedelta

from django.http import JsonResponse
from django.shortcuts import render

from ..devices.models import Device
from ..ingest.models import DataPoint


def all_devices(request):
    devices = [_.as_json() for _ in Device.objects.all()]
    return JsonResponse(devices)

def data_slice(request):
    start_time = datetime.fromisoformat(request.GET.get('start'))
    if 'end' in request.GET:
        end_time = datetime.fromisoformat(request.GET.get('end'))
    else:
        end_time = start_time + timedelta(second=600)

    data = DataPoint.objects.filter(timestamp__gte=start_time, timestamp__lte=end_time).order_by('timestamp')

    return JsonResponse(data)
