from apps.livescore.models import Result
from rest_framework import generics, permissions, status
from rest_framework_bulk import ListBulkCreateUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
import glob, os
from django.conf import settings
import copy
from django.core.mail import send_mail 
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import random
from django.db.models.functions import Lower
from django.utils import timezone
import datetime
import hashlib
from transliterate import translit

from apps.livescore.models import (
    Result,
)
from .serializers import (
    ResultSerializer,
)
from .parsers import (
    get_match_results,
)


class ResultAPIView(generics.ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        response = get_match_results(request.GET['url'])
        return Response(ResultSerializer(
            response,
            many=True
        ).data)