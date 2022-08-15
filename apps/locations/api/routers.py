from rest_framework.routers import DefaultRouter

from apps.locations.api.country.viewsets import CountryViewSet

router = DefaultRouter()

# TODO: Agregar estados y ciudades
router.register('country',CountryViewSet, basename='country')

urlpatterns = router.urls