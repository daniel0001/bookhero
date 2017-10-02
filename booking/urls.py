from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'booking/', booking, name='booking'),

    url(r'^booking-list$', BookingListView.as_view(), name='booking-list'),
    url(r'^(?P<pk>\d+)$', BookingDetailView.as_view(), name='booking-detail'),
    url(r'^add', BookingCreateView.as_view(), name='booking-create'),
    url(r'^(?P<pk>\d+)/edit', BookingUpdateView.as_view(), name='booking-edit'),
    url(r'^(?P<pk>\d+)/delete', BookingDeleteView.as_view(), name='booking-delete'),

]