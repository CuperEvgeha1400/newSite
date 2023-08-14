from django.urls import path
from .api import CreateUserView


urlpatterns = [
    path('register/', CreateUserView.as_view()),
]
