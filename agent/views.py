import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import ActivityLog, Screenshot
import json

def dashboard(request):
    return render(request, 'dashboard.html')



@csrf_exempt
def update_config(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        if hasattr(settings, 'SCREENSHOT_INTERVAL'):
            settings.SCREENSHOT_INTERVAL = int(data.get('interval', settings.SCREENSHOT_INTERVAL))
        
        if hasattr(settings, 'SCREENSHOT_BLUR'):
            settings.SCREENSHOT_BLUR = data.get('blur', settings.SCREENSHOT_BLUR)
        
        if hasattr(settings, 'SCREENSHOT_ENABLED'):
            settings.SCREENSHOT_ENABLED = data.get('enabled', settings.SCREENSHOT_ENABLED)
        
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

logger = logging.getLogger(__name__)

def get_activity_logs(request):
    logs = ActivityLog.objects.order_by('-timestamp')[:50]
    data = [{'timestamp': log.timestamp.isoformat(), 'activity_type': log.activity_type, 'details': log.details} for log in logs]
    logger.info(f"Returning {len(data)} activity logs")
    return JsonResponse(data, safe=False)

def get_screenshots(request):
    screenshots = Screenshot.objects.order_by('-timestamp')[:10]
    data = [{'timestamp': screenshot.timestamp.isoformat(), 'image_path': screenshot.image_path, 'is_blurred': screenshot.is_blurred} for screenshot in screenshots]
    logger.info(f"Returning {len(data)} screenshots")
    return JsonResponse(data, safe=False)