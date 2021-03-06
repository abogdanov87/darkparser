from django.conf.urls import url

from .api.v1 import views as api_v1_views
from . import apps

app_name = apps.WildstatConfig.name

urlpatterns = [
    url(
        r'^api/v1/wildstat/results/$',
        api_v1_views.MatchAPIView.as_view(),
        name='get results',
    ),
]