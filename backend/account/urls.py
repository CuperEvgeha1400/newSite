from django.urls import path
from .views import (
    MyUserView
)

urlpatterns = [
    path('MyUser/', MyUserView.as_view())
]
