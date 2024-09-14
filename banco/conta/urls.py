from django.urls import path
from api.viewsets import ContaViewSet

urlpatterns = [
    path('conta-bancaria/', ContaViewSet.as_view(), name='criar-conta-bancaria'),
]
