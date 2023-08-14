from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import IndexView, OrderAPIViewSet, OrderAddFormView, OrderDetailView, OrderListView

api_router = DefaultRouter()
api_router.register(r'orders', OrderAPIViewSet, basename="orders")

api_urlpatterns = [
    path('', include(api_router.urls))
]

urlpatterns = [
    path('api/v1/', include((api_urlpatterns, 'api-v1'))),
    path('', IndexView.as_view(), name='index'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/add/', OrderAddFormView.as_view(), name='order-add'),
]
