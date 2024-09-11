from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/update-config/', views.update_config, name='update_config'),
    path('api/activity-logs/', views.get_activity_logs, name='get_activity_logs'),
    path('api/screenshots/', views.get_screenshots, name='get_screenshots'),
]
