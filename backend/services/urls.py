from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, MasterViewSet

router = DefaultRouter()
router.register('services', ServiceViewSet)
router.register('masters', MasterViewSet)

urlpatterns = router.urls