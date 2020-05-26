from rest_framework import generics


from .models import Shop
from .permissions import AdminPermission
from .serializers import ShopSerializer


class ShopList(generics.ListCreateAPIView):

    serializer_class = ShopSerializer
    permission_classes = [AdminPermission,]
    queryset = Shop.objects.all()


class ShopDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ShopSerializer
    permission_classes = [AdminPermission,]
    queryset = Shop.objects.all()

