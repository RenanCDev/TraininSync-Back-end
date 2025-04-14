from django.contrib import admin
from django.urls import path, include
from .views import home


urlpatterns = [
    path('', home),
    path("admin/", admin.site.urls),
    path("api/traininsync/", include("traininsync.urls", namespace="traininsync")),
]
