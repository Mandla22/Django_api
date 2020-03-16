from abc import ABC

from rest_framework import serializers
from . models import Usage


class UsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usage
        fields = '__all__'

    def create(self, validated_data):
        return Usage.objects.create(**validated_data)
