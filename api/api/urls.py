from django.conf.urls import include, url
from django.db.models.fields import CharField
from rest_framework import routers
from .views import *

urlpatterns = [
    url(r'^stream_view/$', ScreamView.as_view())
]