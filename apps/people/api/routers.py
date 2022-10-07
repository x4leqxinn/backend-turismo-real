from rest_framework.routers import DefaultRouter
from apps.people.api.employee.employee_views import EmployeeViewSet

router = DefaultRouter()

router.register('employee',EmployeeViewSet, basename='employee')

urlpatterns = router.urls

