from django.conf.urls import include, url
from rest_framework import routers
from shoes.views import ShoeColorViewSet, ManufacturerViewSet, ShoeTypeViewSet, ShoeViewSet

router = routers.DefaultRouter()
router.register('manufacturer', ManufacturerViewSet)
router.register('shoecolor', ShoeColorViewSet)
router.register('shoetype', ShoeTypeViewSet)
router.register('shoe', ShoeViewSet)

urlpatterns = [
    url(r'^shoes', include(router.urls))
]