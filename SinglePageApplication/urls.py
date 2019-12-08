from django.conf.urls import include, url
from SinglePageApplication.views import index

urlpatterns = [
    url('^$', index),
]
