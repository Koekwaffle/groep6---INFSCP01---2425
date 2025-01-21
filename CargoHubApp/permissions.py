from rest_framework import permissions
from api.providers import auth_provider

class APIKeyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return False
        
        api_key = auth_header.split(' ')[1]
        user = auth_provider.get_user(api_key)
        return user is not None
