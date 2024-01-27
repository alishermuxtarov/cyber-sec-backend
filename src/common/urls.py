from django.urls import path
from . import views

urlpatterns = [
    path('hosts/', views.HostList.as_view(), name='host-list'),
    path('keywords/', views.KeywordList.as_view(), name='keyword-list'),
]