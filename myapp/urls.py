from django.conf.urls import url
from .views import JhumkaList

urlpatterns = [
    url(r'^jhumkas/$', JhumkaList.as_view(), name='jhumka-list'),
    # Add more URL patterns if needed
]
