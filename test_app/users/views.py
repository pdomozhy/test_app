from rest_framework import generics, views, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


from .models import User
from .permissions import AdminPermission
from .serializers import (
    UserSerializer,
    RestrictedUserSerializer,
    UserRegisterSerializer,
    UserConfirmSerializer,
)


class UserList(generics.ListCreateAPIView):

    serializer_class = UserSerializer
    permission_classes = [AdminPermission, ]
    queryset = User.objects.all()


class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = UserSerializer
    permission_classes = [AdminPermission, ]
    queryset = User.objects.all()


class RestrictedUserDetail(generics.RetrieveUpdateAPIView):

    serializer_class = RestrictedUserSerializer

    def get_object(self):
        return self.request.user


class UserRegisterView(views.APIView):

    permission_classes = [AllowAny,]
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)


class UserConfirmView(views.APIView):

    permission_classes = [AllowAny,]
    serializer_class = UserConfirmSerializer

    def put(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        email = serializer.validated_data.get('email')
        token = serializer.validated_data.get('app_id')
        user = User.objects.filter(email=email, app_id=token).first()
        if not user:
            body = {'deteils': 'INCORRECT_TOKEN'}
            return Response(body, status.HTTP_400_BAD_REQUEST)
        user.is_confirmed = True
        user.save()
        return Response(serializer.data, status.HTTP_200_OK)
