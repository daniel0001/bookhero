from django.conf.urls import url
from .views import booking

urlpatterns = [
    url(r'booking/', booking, name='booking'),

]