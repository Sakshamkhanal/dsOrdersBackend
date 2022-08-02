from rest_framework import routers
from django.urls import path,include
from dsorders.api.ViewSets import *
from knox import views as knox_views
router = routers.DefaultRouter()
router.register(r'dealer',DealerViewSet,basename='dealer')
router.register(r'salesman',SalesmanViewSet,basename='salesman')
router.register(r'items',ItemsViewSet,basename='items')
router.register(r'order',OrderViewset,basename='order')
router.register(r'shop',ShopViewSet,basename='shop')
router.register(r'orderitems',orderItemViewSet,basename='orderitems')

urlpatterns = [
    path('api/auth/login',LoginAPI.as_view()),
    path('api/auth/user',UserAPI.as_view()),
    path('api/auth/logout',knox_views.LogoutView.as_view(),name='knox_logout'),
    path('api/',include(router.urls)),
]
