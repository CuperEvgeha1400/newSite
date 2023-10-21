from django.urls import path
from .views import MyUserView, TokenView

urlpatterns = [
    path('MyUser/', MyUserView.as_view()),
    path('TokenView/', TokenView)
]
