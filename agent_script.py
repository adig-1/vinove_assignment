import time
import django
import os
import sys

# Set up Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "activity_tracker.settings")
django.setup()

from django.conf import settings
from agent.utils import capture_screenshot, log_activity, get_system_info

def run_agent():
    print("Agent started")
    log_activity("Agent Started")
    
    while True:
        print("Agent loop running")
        if settings.SCREENSHOT_ENABLED:
            print("Capturing screenshot")
            capture_screenshot(blur=settings.SCREENSHOT_BLUR)
        
        print("Logging activity")
        log_activity("Agent Running", "Regular check-in")
        
        time.sleep(settings.SCREENSHOT_INTERVAL)

if __name__ == "__main__":
    run_agent()