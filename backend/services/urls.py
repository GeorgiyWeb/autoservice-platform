from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, MasterViewSet, BookingViewSet

router = DefaultRouter()
router.register('services', ServiceViewSet)
router.register('masters', MasterViewSet)
router.register('bookings', BookingViewSet)

urlpatterns = router.urls   