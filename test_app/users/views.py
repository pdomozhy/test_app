from rest_framework import generics


from .models import User
from .permissions import AdminPermission
from .serializers import UserSerializer, RestrictedUserSerializer


class UserList(generics.ListCreateAPIView):

    serializer_class = UserSerializer
    permission_classes = [AdminPermission,]
    queryset = User.objects.all()


class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = UserSerializer
    permission_classes = [AdminPermission,]
    queryset = User.objects.all()


class RestrictedUserDetail(generics.RetrieveUpdateAPIView):

    serializer_class = RestrictedUserSerializer

    def get_object(self):
        return self.request.user
