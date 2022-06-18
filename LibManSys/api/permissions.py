from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            return bool(request.user and request.user.is_admin)
        except:
            return False

class AllowAll(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            return bool(request.user )
        except:
            return False

class AllowAny(permissions.BasePermission):

    def has_permission(self, request, view):
        return True
