from rest_framework import serializers
from mobile.models import Mobile


class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mobile
        fields="__all__"
        read_only_fields=["id"]