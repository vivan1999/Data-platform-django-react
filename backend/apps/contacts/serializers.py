from rest_framework import serializers

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
        return super().create(validated_data)
    def validate(self, attrs):
        return super().validate(attrs)
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)




