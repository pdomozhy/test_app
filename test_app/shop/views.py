from rest_framework import generics


from users.permissions import AdminPermission
from .models import Shop
from .serializers import ShopSerializer


class ShopList(generics.ListCreateAPIView):

    serializer_class = ShopSerializer
    permission_classes = [AdminPermission,]
    queryset = Shop.objects.all()


class ShopDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ShopSerializer
    permission_classes = [AdminPermission,]
    queryset = Shop.objects.all()

