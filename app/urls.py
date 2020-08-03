from django.urls import path
from django.conf.urls import include
from django.contrib import admin

from rest_framework import routers

from crm.viewsets import CustomerList, EventList

router = routers.DefaultRouter()
router.register("customers", CustomerList, basename="customers")
router.register("events", EventList, basename="events")


urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("admin/", admin.site.urls)
]
