
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Booking
from .forms import BookingForm
from django.urls import reverse_lazy
# Create your views here.
# def booking(request):
#     return render(request, 'booking.html')



class BookingListView(ListView):
    template_name = "booking/booking-list.html"
    model = Booking
    paginate_by = 5


class BookingDetailView(DetailView):
    template_name = "booking/booking-detail.html"
    model = Booking


class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm

    def form_valid(self, form):
        """
        Assign the customer to the request.user
        """
        form.instance.customer = self.request.user
        """
        Assign the merchant = testing uses merchant as 999
        """
        return super(BookingCreateView, self).form_valid(form)



class BookingUpdateView(UpdateView):
    model = Booking
    fields = ['name', 'email', 'image']


class BookingDeleteView(DeleteView):
    model = Booking
    success_url = reverse_lazy('booking-list')