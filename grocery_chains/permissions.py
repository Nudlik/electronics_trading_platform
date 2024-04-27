from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS


class IsActive(IsAuthenticated):

    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.is_active


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user
