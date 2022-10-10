from rest_framework.routers import DefaultRouter
from apps.people.api.client.client_views import ClientViewSet
from apps.people.api.employee.employee_views import EmployeeViewSet

router = DefaultRouter()

router.register('employee',EmployeeViewSet, basename='employee')
router.register('client',ClientViewSet, basename='client')

urlpatterns = router.urls

