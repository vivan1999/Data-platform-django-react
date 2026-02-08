from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
User = get_user_model()

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    notes = serializers.CharField()
    is_staff = serializers.BooleanField()
    is_active = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    modified_at = serializers.DateTimeField()
    def create(self, validated_data):
        user,created = User.objects.get_or_create(email = validated_data["email"], defaults= {**validated_data})
        return user
    def validate(self, attrs):
        return super().validate(attrs)
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "email","first_name","password")





