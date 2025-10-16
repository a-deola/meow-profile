from django.urls import path
from .views import profile_data

urlpatterns = [
    path("me", profile_data, name="profile"),
]
