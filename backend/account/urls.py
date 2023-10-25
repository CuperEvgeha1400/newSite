from django.urls import path
from .views import MyUserView, TokenView, SignupVerify

urlpatterns = [
    path('MyUser/', MyUserView.as_view()),
    path('TokenView/', TokenView),
    path('SignupVerify/', SignupVerify.as_view())
]
