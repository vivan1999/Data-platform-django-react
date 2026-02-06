from django.urls import path
from .views import UserContact

urlpatterns = [
    path("",UserContact.as_view())
]