from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify

class Events(models.Model):
    name = models.CharField(max_length=1000)
    file = models.FileField(blank=True, upload_to="Events")
    slug = models.SlugField(blank=False, max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    link = models.URLField(blank=True )
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = "Events"
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Events, self).save(*args, **kwargs)

    
    
    def get_absolute_url(self):
        return reverse('events')
    