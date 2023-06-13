from rest_framework import permissions

from rest_framework.views import Request, View
from .models import Movie


class MyCustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and request.user.is_superuser


class permissionDelete(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Movie):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and request.user.is_superuser
