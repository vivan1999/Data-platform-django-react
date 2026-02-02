from django.urls import path
from .views import DeviceView,getDeviceData

urlpatterns = [
    path("",DeviceView.as_view()),
    path("function/", getDeviceData)
]