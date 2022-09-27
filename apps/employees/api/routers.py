from rest_framework.routers import DefaultRouter

from apps.employees.api.position.views import PositionViewSet
from apps.employees.api.employee.views import EmployeeViewSet

router = DefaultRouter()

router.register('position',PositionViewSet, basename='position')
router.register('employee',EmployeeViewSet, basename='employee')

urlpatterns = router.urls

