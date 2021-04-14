from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify

class Videos(models.Model):
    name = models.CharField(max_length=1000)
    file = models.FileField(blank=True,null=True, upload_to="Events")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=False, max_length=1000)
    link = models.URLField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = "Videos"
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Videos, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('videos')

@receiver(pre_save, sender=Videos)
def save_presentation(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)
    