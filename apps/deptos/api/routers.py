from rest_framework.routers import DefaultRouter

from apps.deptos.api.depto_views import InventoryViewSet

router = DefaultRouter()

router.register('inventory',InventoryViewSet, basename='inventory')

urlpatterns = router.urls