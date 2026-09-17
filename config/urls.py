from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from students.views import (
    StudentViewSet,
    CompanyViewSet,
    PlacementViewSet
)


router = DefaultRouter()

router.register('students', StudentViewSet)
router.register('companies', CompanyViewSet)
router.register('placements', PlacementViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
