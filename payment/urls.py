from django.conf.urls import url
from .views import payment

urlpatterns = [
    url(r'payment/', payment, name='payment'),

]