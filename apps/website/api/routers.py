from rest_framework.routers import DefaultRouter
from apps.website.api.data_analysis.data_views import DataframeViewset


router = DefaultRouter()

router.register('dataframe',DataframeViewset, basename='dataframe')

urlpatterns = router.urls

