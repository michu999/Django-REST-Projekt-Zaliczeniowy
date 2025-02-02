from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apteka.views import LekViewSet

router = DefaultRouter()
router.register(r'leki', LekViewSet, basename='lek')

urlpatterns = [
    path('', include(router.urls)),
]
