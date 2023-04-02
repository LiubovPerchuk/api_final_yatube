from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    """Класс разрешений для доступа только автору объекта."""

    def has_object_permission(self, request, view, obj):
        """Метод предоставляет разрешение автору объекта."""
        return (obj.author == request.user
                or request.method in permissions.SAFE_METHODS)
