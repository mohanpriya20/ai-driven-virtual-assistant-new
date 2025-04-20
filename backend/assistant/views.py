from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DetectionLog

class DetectionLogView(APIView):
    def get(self, request):
        logs = DetectionLog.objects.all().values()
        return Response(list(logs))