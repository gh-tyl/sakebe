from django.conf.urls import include, url
from django.db.models.fields import CharField
from rest_framework import routers
from .views import *

urlpatterns = [
    url(r'^scream_list/$', ScreamListView.as_view()),
    url(r'^scream_register/$', ScreamRegisterView.as_view()),
    url(r'^scream_upload/$', ScreamUploadView.as_view()),
]