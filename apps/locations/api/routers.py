from rest_framework.routers import DefaultRouter
from apps.locations.api.city.views import CityViewSet

from apps.locations.api.country.views import CountryViewSet
from apps.locations.api.state.views import StateViewSet

router = DefaultRouter()

router.register('countries',CountryViewSet, basename='countries')
router.register('states',StateViewSet, basename='states')
router.register('cities',CityViewSet, basename='cities')

urlpatterns = router.urls