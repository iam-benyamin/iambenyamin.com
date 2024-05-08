from rest_framework.serializers import ModelSerializer
from home.models.service import Service


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ['title']
