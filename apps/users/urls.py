from django.urls import path

from apps.users.views import (
    AdminToUserView,
    UserBlockView,
    UserListCreateAPIView,
    UserRetrieveUpdateDestroyAPIView,
    UserToAdminView,
    UserUnblockView,
)

urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='use_list_create'),
    path('/<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view(), name='user_retrieve-update-destroy'),
    path('/<int:pk>/to_admin', UserToAdminView.as_view(), name='user_to_admin'),
    path('/<int:pk>/to_user', AdminToUserView.as_view(), name='admin_to_user'),
    path('/<int:pk>/block', UserBlockView.as_view(), name='user_to_block'),
    path('/<int:pk>/unblock', UserUnblockView.as_view(), name='user_to_unblock'),
]
