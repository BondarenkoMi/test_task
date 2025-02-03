
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.views import VPSViewSet

router = DefaultRouter()
router.register('vps', VPSViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
