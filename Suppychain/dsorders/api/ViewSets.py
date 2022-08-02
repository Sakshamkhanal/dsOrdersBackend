from multiprocessing import context
from sys import api_version
from rest_framework import status,permissions,generics
from django.shortcuts import get_object_or_404
from html5lib import serialize
from dsorders.api.serializers import DealerSerializer, OrderItemSerializer,SalesmanSerilizer,ItemSerilizer,OrderSerializer, ShopSerializer,UserSerializer,LoginSerializer
from dsorders.models import Dealer,Item, Order,Salesman, Shop, orderItems
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from knox.auth import AuthToken
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.authtoken.serializers import AuthTokenSerializer

#User API
class LoginAPI(generics.GenericAPIView):
   # permission_classes =[HasAPIKey]
    serializer_Class = LoginSerializer

    def post(self,request, *args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response
        (
            {
                "user":UserSerializer(user,context=self.get_serializer_context()).data,"token":AuthToken.objects.create(user)[1]
            }
        )

class UserAPI(generics.RetrieveAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user



#Models viewsets
class DealerViewSet(ModelViewSet):
    serializer_class = DealerSerializer
    http_method_names = ['get', 'post', 'put',
                         'patch', 'head', 'options', 'trace']

    def get_queryset(self):
        queryset = Dealer.objects.all()
        return queryset


class SalesmanViewSet(ModelViewSet):
    serializer_class = SalesmanSerilizer

    http_method_names = ['get', 'post', 'put',
                         'patch', 'delete', 'head', 'options', 'trace']

    def get_queryset(self):
        query_set = Salesman.objects.all()
        return query_set

class ItemsViewSet(ModelViewSet):
    serializer_class = ItemSerilizer

    http_method_names = ['get', 'post', 'put',
                         'patch', 'delete', 'head', 'options', 'trace']

    def get_queryset(self):
        query_set =  Item.objects.all()
        return query_set
        
class OrderViewset(ModelViewSet):
    serializer_class = OrderSerializer

    http_method_names = ['get', 'post', 'put',
                         'patch', 'delete', 'head', 'options', 'trace']

    def get_queryset(self):
        query_set = Order.objects.all()
        return query_set


class ShopViewSet(ModelViewSet):
    serializer_class = ShopSerializer

    http_method_names = ['get', 'post', 'put',
                         'patch', 'delete', 'head', 'options', 'trace']
    
    def get_queryset(self):
        query_set = Shop.objects.all()
        return query_set

class orderItemViewSet(ModelViewSet):
        serializer_class = OrderItemSerializer

        http_method_names = ['get', 'post', 'put',
                         'patch', 'delete', 'head', 'options', 'trace']

        def get_queryset(self):
            query_Set = orderItems.objects.all()
            return query_Set