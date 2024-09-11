import os
import pyautogui
from PIL import Image, ImageFilter
from django.conf import settings
from django.utils import timezone
from .models import ActivityLog, Screenshot

def capture_screenshot(blur=False):
    timestamp = timezone.now()
    filename = f"screenshot_{timestamp.strftime('%Y%m%d_%H%M%S')}.png"
    filepath = os.path.join(settings.SCREENSHOT_DIR, filename)
    
    screenshot = pyautogui.screenshot()
    if blur:
        screenshot = screenshot.filter(ImageFilter.GaussianBlur(radius=10))
    screenshot.save(filepath)
    
    Screenshot.objects.create(
        timestamp=timestamp,
        image_path=filepath,
        is_blurred=blur
    )
    
    return filepath

def log_activity(activity_type, details=""):
    ActivityLog.objects.create(
        activity_type=activity_type,
        details=details
    )

def get_system_info():
    # Implement logic to get system information
    pass


