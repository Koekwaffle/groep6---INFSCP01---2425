from django.db import models
import secrets
from django.http import JsonResponse

class Device(models.Model):
    name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=50, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.api_key:
            self.api_key = secrets.token_urlsafe(32)  
        super().save(*args, **kwargs)

class DeviceAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        api_key = request.headers.get("Authorization")
        if not api_key or not api_key.startswith("Bearer "):
            return JsonResponse({"error": "Unauthorized"}, status=401)

        api_key_value = api_key.split("Bearer ")[1]
        try:
            device = Device.objects.get(api_key=api_key_value)
            request.device = device  # Attach device info to the request
        except Device.DoesNotExist:
            return JsonResponse({"error": "Invalid API key"}, status=403)

        return self.get_response(request)
    
#TODO 
# MAKE DEVICES HAVE UNIQUE ENDPOINTS
# MAKE DEVICES HAVE UNIQUE API KEYS
# MAKE DEVICES HAVE LIMITED DATA ACCESS
