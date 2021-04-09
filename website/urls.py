from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.viewset_api import *


router = routers.DefaultRouter()
router.register('kelompok', KelompokViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
