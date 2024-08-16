from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register('your-endpoint', views.YourViewSet) # 뷰셋을 추가할 때마다 이런 식으로 등록하세요

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]