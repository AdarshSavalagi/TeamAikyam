from django.test import RequestFactory
from django.urls import reverse
from rest_framework.views import APIView, Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes, api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from django.db import IntegrityError
from core.models import *
from core.serializers import *


class index(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {}

        user_instance = request.user
        user_serializer = CustomUserSerializer(user_instance).data
        data['userSerializer'] = user_serializer

        investments_queryset = Investment.objects.filter(level=user_instance.level)
        investment_serializer = InvestmentSerializer(investments_queryset, many=True).data
        data['investmentSerializer'] = investment_serializer

        insurances_queryset = Insurance.objects.filter(level=user_instance.level)
        insurance_serializer = InsuranceSerializer(insurances_queryset, many=True).data
        data['insuranceSerializer'] = insurance_serializer

        consultancies_queryset = Consultancy.objects.filter(level=user_instance.level)
        consultancy_serializer = ConsultancySerializer(consultancies_queryset, many=True).data
        data['consultancySerializer'] = consultancy_serializer

        return Response(data)



@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    if request.method == 'POST':
        name = request.data.get('name', '')
        income = request.data.get('income', '')
        expense = request.data.get('expense', '')
        asset = request.data.get('asset', '')
        loan = request.data.get('loan', '')
        email = request.data.get('email', '')
        financial_goal = request.data.get('financial_goal', '')
        password = request.data.get('financial_goal', '')
        try:
            user = CustomUser.objects.create_user(
                password=email, email=email, first_name=name, income=income, expense=expense, asset=asset, loan=loan, financial_goal=financial_goal)

            factory = RequestFactory()
            context = {'username': email, 'password': password}
            request = factory.post(reverse('token_obtain_pair'),
                                   data=request.data, format='json', **context)
            token_obtain_pair_view = TokenObtainPairView.as_view()
            response = token_obtain_pair_view(request)
            return Response(response.data)
        except IntegrityError:
            return Response({"message": "user already exists"})
    return Response("Invalid request :-> only post requests are allowed")
