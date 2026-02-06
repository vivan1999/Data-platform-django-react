from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    def create(self, validated_data):
        return super().create(validated_data)
    def validate(self, attrs):
        return super().validate(attrs)
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
class ContactSerializer(serializers.Serializer):
    user = UserSerializer()
    address = serializers.CharField()
    def create(self, validated_data):
        return super().create(validated_data)
    def validate(self, attrs):
        return super().validate(attrs)
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)



