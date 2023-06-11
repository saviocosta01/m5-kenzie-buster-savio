from django.urls import path
from .views import UserView, LoginUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
]
