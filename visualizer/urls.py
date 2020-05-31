from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.visualize, name="visualize"),
    url('atlas/',views.atlas, name="atlas"),
]