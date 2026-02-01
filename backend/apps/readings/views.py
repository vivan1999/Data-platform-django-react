from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import *
from .serializers import DeviceSerializer

from rest_framework.permissions import AllowAny
# Create your views here.

class DeviceView(ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return super().get_queryset()