from requests import request
from rest_framework import generics, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from authemail import wrapper
from .models import User
from .serializer import MyUserSerializer


@permission_classes([IsAuthenticated])
class MyUserView(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = MyUserSerializer

@api_view(['GET'])
def TokenView(request):
    email = request.data.get('email')
    print(email)
    password = request.data.get('password')
    print(password)
    account = wrapper.Authemail()
    response = account.login(email=email, password=password)
    return Response(response)
