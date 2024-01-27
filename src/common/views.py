from rest_framework import generics
from .models import Host, Keyword
from .serializers import HostSerializer, KeywordSerializer


class HostList(generics.ListAPIView):
    queryset = Host.objects.all().order_by("id")
    serializer_class = HostSerializer


class KeywordList(generics.ListAPIView):
    queryset = Keyword.objects.all().order_by("id")
    serializer_class = KeywordSerializer
