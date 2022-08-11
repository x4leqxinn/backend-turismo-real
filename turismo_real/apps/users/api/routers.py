from rest_framework.routers import DefaultRouter

from apps.users.api.views.users_views import UserViewSet

router = DefaultRouter()

router.register('',UserViewSet, basename='users')

urlpatterns = router.urls