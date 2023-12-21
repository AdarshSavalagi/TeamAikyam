from django.urls import path
from .views import *
urlpatterns = [
    path('api/',index.as_view()),
    path('create-user/',create_user),

]
