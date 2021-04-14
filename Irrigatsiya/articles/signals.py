from django.db.models.signals import pre_save
from .models import Articles
from django.dispatch import receiver
from django.utils.text import slugify

@receiver(pre_save, sender=Articles)
def object_slug_updated(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)
