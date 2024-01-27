from rest_framework import serializers
from .models import Host, Keyword


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ("url", "category", "risk_level")


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ("keyword", "category", "allowed_for_host")
