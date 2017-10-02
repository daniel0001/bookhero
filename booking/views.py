
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Booking
from django.urls import reverse_lazy
# Create your views here.
def booking(request):
    return render(request, 'booking.html')



class BookingListView(ListView):
    model = Booking
    paginate_by = 5


class BookingDetailView(DetailView):
    model = Booking


class BookingCreateView(CreateView):
    model = Booking
    fields = ['name', 'email', 'image']


class BookingUpdateView(UpdateView):
    model = Booking
    fields = ['name', 'email', 'image']


class BookingDeleteView(DeleteView):
    model = Booking
    success_url = reverse_lazy('booking-list')