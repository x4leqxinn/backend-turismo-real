from rest_framework.routers import DefaultRouter

from apps.users.api.client.views.clients_views import ClientViewSet

router = DefaultRouter()

router.register('client',ClientViewSet, basename='client')

urlpatterns = router.urls