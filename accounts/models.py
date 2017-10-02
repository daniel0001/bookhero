from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import arrow


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    stripe_id = models.CharField(max_length=40, default='')
    #subscription_end = models.DateTimeField(default=arrow.now)

    # @property
    # def subscription_active(self):
    #     return self.subscription_end > arrow.now()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# # Create your models here.
# class CustomerProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer_profile")
#     stripe_id = models.CharField(max_length=40, default='')

# @receiver(post_save, sender=User)
# def create_customer_profile(sender, instance, created, **kwargs):
#     if created:
#         CustomerProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_customer_profile(sender, instance, **kwargs):
#     instance.profile.save()




# class MerchantProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="merchant_profile")
#     stripe_id = models.CharField(max_length=40, default='')
#     stripe_connect_id = models.CharField(max_length=40, default='')
#     #subscription_end = models.DateTimeField(default=arrow.now)

#     # @property
#     # def subscription_active(self):
#     #     return self.subscription_end > arrow.now()


# @receiver(post_save, sender=User)
# def create_merchant_profile(sender, instance, created, **kwargs):
#     if created:
#         MerchantProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_merchant_profile(sender, instance, **kwargs):
#     instance.profile.save()