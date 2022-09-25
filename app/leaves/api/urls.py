from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import viewsets

router = SimpleRouter()
router.register(r'', viewsets.LeaveViewset, basename='leave')


urlpatterns = router.get_urls()
