from rest_framework import serializers

class DeviceSerializer(serializers.Serializer):
    device_id = serializers.CharField()
    name = serializers.CharField()
    type = serializers.CharField()
    location = serializers.CharField()
    is_active = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    modified_at = serializers.DateTimeField()

    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)