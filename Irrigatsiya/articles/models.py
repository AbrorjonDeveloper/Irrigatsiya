from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Articles(models.Model):
    name = models.CharField(max_length=500)
    article = models.FileField(blank=True, upload_to="articles")
    slug = models.SlugField(blank=False, null=False, unique=True, max_length=500)
    link = models.URLField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Articles'
    
    def save(self, *args, **kwargs):
        if  not self.slug :
            self.slug = slugify(self.name)
        return super(Articles, self).save(*args, **kwargs)

    def class_name(self):
        return self.__class__.__name__

    def get_absolute_url(self):
        return reverse("articles")
     