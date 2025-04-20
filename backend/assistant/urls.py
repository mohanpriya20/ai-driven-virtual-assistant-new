from django.urls import path
from .views import DetectionLogView

urlpatterns = [path('logs/', DetectionLogView.as_view())]