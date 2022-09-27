from rest_framework.routers import DefaultRouter

from apps.employees.api.position.views import PositionViewSet

router = DefaultRouter()

router.register('position',PositionViewSet, basename='position')

urlpatterns = router.urls

