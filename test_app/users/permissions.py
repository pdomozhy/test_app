from rest_framework.permissions import BasePermission


from .constants import ADMIN


class UserPermission(BasePermission):

    def has_permission(self, request, view):

        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.is_confirmed
        )


class ApplicantPermission(BasePermission):

    def has_permission(self, request, view):

        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.is_confirmed and
            request.user.role == ADMIN
        )
