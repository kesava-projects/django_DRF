import profile

from django.urls import path
from .views import register, login, profile, update_profile, delete_profile

urlpatterns = [
    # path("login", login),
    path("register", register),
    path("login", login),
    path("profile", profile),
    path("update", update_profile),
    path("delete", delete_profile)
]