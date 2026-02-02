from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import *
from .serializers import DeviceSerializer
import json
from django.http import HttpResponse,JsonResponse
from rest_framework.permissions import AllowAny
# Create your views here.

class DeviceView(ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Device.objects.all()

def getDeviceData(request,**kwargs):
    devices = Device.objects.all()
    serialized_data = DeviceSerializer(devices,many = True)
    return JsonResponse(serialized_data.data,safe=False)