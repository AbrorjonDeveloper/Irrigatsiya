from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify

class Projects(models.Model):
    name = models.CharField(max_length=600)
    file = models.FileField(blank=True,upload_to="projects")
    link = models.URLField(blank=True)
    slug = models.SlugField(max_length=600)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)
     
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Projects, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('projects')