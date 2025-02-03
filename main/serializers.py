from .models import VPS
from rest_framework import serializers


class VPSSerializer(serializers.ModelSerializer):

    class Meta:
        model = VPS
        fields = '__all__'