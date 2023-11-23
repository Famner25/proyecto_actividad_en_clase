from django.urls import path, include
from rest_framework import routers
from .views import ProductosViewSet
from .views import TipoProductosViewSet


router= routers.DefaultRouter()
router.register(r'metodopago',ProductosViewSet)
router.register(r'citas', TipoProductosViewSet)

urlpatterns =[

    path('', include(router.urls))
]
