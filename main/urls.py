from django.conf.urls import url, include
from .views import get_data

urlpatterns = [
    url(r'', get_data, name='ListData')
]
