from django.contrib import admin

from .models import ActivityLog,Screenshot

# Register your models here.
admin.site.register(ActivityLog)
admin.site.register(Screenshot)