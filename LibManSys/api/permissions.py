from rest_framework import permissions
from accounts.models import User

class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if User.objects.filter(email=request.user):
            return bool(request.user.is_admin)
        return False

class AllowAll(permissions.BasePermission):

    def has_permission(self, request, view):
        return True

class IsUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if User.objects.filter(email=request.user):
            return True
        return False




