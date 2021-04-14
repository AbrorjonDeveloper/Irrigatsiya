from django.db import models 
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify

class Presentations(models.Model):
    name = models.CharField(max_length=700)
    file = models.FileField(blank=True, upload_to="presentations")
    slug = models.SlugField(null=False, unique=True, max_length=700)
    link = models.URLField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Presentation'
        verbose_name_plural = 'Presentations'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Presentations, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('presentations')