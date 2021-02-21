import secrets

from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import User, Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a profile for the user
        Profile.objects.create(user=instance, username='guest' + secrets.token_hex(4))

    instance.profile.save()
