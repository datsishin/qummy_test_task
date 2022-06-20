from rest_framework import serializers

from api.models import SecretKey


class SecretKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = SecretKey
        fields = '__all__'
