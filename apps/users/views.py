from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from core.permissions.custom_permissions import IsAdminOrWriteOnly, IsSuperUser

from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer

UserModel: User = get_user_model()


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAdminOrWriteOnly,)


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAdminUser,)


class UserToAdminView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            return Response({'details': 'already exist is_staff=True'}, status=status.HTTP_400_BAD_REQUEST)
        user.is_staff = True
        user.save()
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AdminToUserView(UserToAdminView):

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            return Response({'details': 'already exist is_staff=False'}, status=status.HTTP_400_BAD_REQUEST)
        user.is_staff = False
        user.save()
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserBlockView(UserToAdminView):
    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            return Response({'details': 'already exist is_active=False'}, status=status.HTTP_400_BAD_REQUEST)
        user.is_active = False
        user.save()
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserUnblockView(UserToAdminView):
    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            return Response({'details': 'already exist is_active=True'}, status=status.HTTP_400_BAD_REQUEST)
        user.is_active = True
        user.save()
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
