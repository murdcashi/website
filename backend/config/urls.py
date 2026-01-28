from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("src.modules.core.interface.urls")),
    path("api/holdings/", include("src.modules.holdings.interface.urls")),
]
