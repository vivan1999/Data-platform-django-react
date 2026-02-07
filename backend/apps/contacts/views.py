from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
class UserView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def get_queryset(self):
        return super().get_queryset()