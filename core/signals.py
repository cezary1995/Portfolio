from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.index import ProfilePicture


# Signal receiver
@receiver(post_save, sender=ProfilePicture)
def ensure_single_display_picture(sender, instance, **kwargs):
    # If current obj has 'display=True', then set False for all other objs
    if instance.display:
        ProfilePicture.objects.exclude(id=instance.id).update(display=False)