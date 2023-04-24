from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import ActivityLog
from activity_log.serializers import ActivityLogSerializer


class ActivityLogReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer