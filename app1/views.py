from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

class UserViewSet(ModelViewSet):
    queryset = App_user.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

