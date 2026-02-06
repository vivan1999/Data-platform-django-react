from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
class UserContact(ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [AllowAny]

    def get_queryset(self):
        return super().get_queryset()