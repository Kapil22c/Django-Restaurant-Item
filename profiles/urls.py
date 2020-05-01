from .views import ProfileDetailView

from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    re_path('(?P<username>[\w-]+)/', ProfileDetailView.as_view(), name='detail'),
]