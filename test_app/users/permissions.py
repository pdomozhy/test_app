from rest_framework.permissions import BasePermission


from .constants import ADMIN


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_authenticated and user.is_confirmed)


class AdminPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_authenticated and user.is_confirmed and \
            user.role == ADMIN)
