from django.db import models
from django.urls import reverse
from django.utils import timezone
from accounts.models import User 


# Create your models here.

class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    merchant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='merchant')
    start_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['merchant']

    def get_absolute_url(self):
        return reverse('booking-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "%s %s" % (self.cutomer.first_name, self.customer.last_name)

