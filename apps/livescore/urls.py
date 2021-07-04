from django.conf.urls import url

from .api.v1 import views as api_v1_views
from . import apps

app_name = apps.LivescoreConfig.name

urlpatterns = [
    url(
        r'^api/v1/results/$',
        api_v1_views.ResultAPIView.as_view(),
        name='get results',
    ),
]