from django.urls import path
from .views import page_detail

urlpatterns = [
    path("pages/<slug:slug>/", page_detail),
]
