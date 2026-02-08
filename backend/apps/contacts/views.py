from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

User = get_user_model()

# Create your views here.
class UserView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def get_queryset(self):
        return super().get_queryset()