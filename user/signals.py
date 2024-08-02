from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print('Creating profile for', instance)
        Profile.objects.create(staff=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    print('Saving profile for', instance)
    instance.profile.save()
