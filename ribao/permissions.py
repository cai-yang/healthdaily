from rest_framework import permissions
from ribao.models import *
class IsOwnerOrReadOnly(permissions.BasePermission):
    """

    """

    def has_object_permission(self, request, view, obj):
        #SAFE_METHODS:get head options
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user

class IsPatientOwnerOrReadOnly(permissions.BasePermission):
    """

    """

    def has_object_permission(self, request, view, obj):
        #SAFE_METHODS:get head options
        if request.method in permissions.SAFE_METHODS:
            return obj.owner == request.user

        return obj.patient.owner == request.user
