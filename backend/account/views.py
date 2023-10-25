from requests import request
from rest_framework import generics, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from authemail.models import SignupCode, EmailChangeCode, PasswordResetCode
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


class SignupVerify(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        code = request.GET.get('code', '')
        verified = SignupCode.objects.set_user_is_verified(code)

        if verified:
            try:
                signup_code = SignupCode.objects.get(code=code)
                signup_code.delete()
            except SignupCode.DoesNotExist:
                pass
            content = {'success': ('Email address verified.')}
            return Response(content, status=status.HTTP_200_OK)
        else:
            content = {'detail': ('Unable to verify user.')}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
