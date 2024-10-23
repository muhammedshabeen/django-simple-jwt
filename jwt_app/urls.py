from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path('register',Register.as_view(),name="register"),
    path('login',TokenObtainPairView.as_view(),name="login"),
    path('login-check',LoginCheck.as_view(),name="login_check"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify', TokenVerifyView.as_view(), name='token_verify'),
    path('logout', LogoutView.as_view(), name='logout'),
]
