from requests import request
from rest_framework import generics
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User
from .serializer import MyUserSerializer


@permission_classes([IsAuthenticated])
class MyUserView(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = MyUserSerializer

