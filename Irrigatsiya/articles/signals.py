from django.db.models.signals import pre_save, pre_delete
from .models import Articles
from django.dispatch import receiver
from django.utils.text import slugify

@receiver(pre_save, sender=Articles)
def object_slug_updated(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)

@receiver(pre_delete, sender=Articles)
def object_file_delete(sender, instance, **kwargs):
    if instance.article:
        instance.article.delete()
