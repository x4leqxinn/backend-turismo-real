from rest_framework.routers import DefaultRouter
from apps.business.api.bookings.bookings_views import BookingViewSet
from apps.business.api.dwelling.dwelling_views import DwellingViewSet
from apps.business.api.inventory.inventory_views import InventoryViewSet
from apps.business.api.services.services_views import ServiceViewSet

router = DefaultRouter()

router.register('inventory', InventoryViewSet, basename='inventory')
router.register('dwelling', DwellingViewSet, basename='dwelling')
router.register('booking',BookingViewSet, basename='booking')
router.register('service',ServiceViewSet, basename='service')

urlpatterns = router.urls