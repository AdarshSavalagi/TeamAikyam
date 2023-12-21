from rest_framework.serializers import ModelSerializer
from .models import *

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
class InvestmentSerializer(ModelSerializer):
    class Meta:
        model=Investment
        fields='__all__'
class InsuranceSerializer(ModelSerializer):
    class Meta:
        model=Insurance
        fields='__all__'
class ConsultancySerializer(ModelSerializer):
    class Meta:
        model=Consultancy
        fields='__all__'