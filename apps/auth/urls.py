from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ActivateAccountView, ChangePasswordView, ResetPasswordView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('/activate/<str:token>', ActivateAccountView.as_view(), name='token'),
    path('/reset_password', ResetPasswordView.as_view(), name='reset_password'),
    path('/change_password/<str:token>', ChangePasswordView.as_view(), name='change_password'),
]
