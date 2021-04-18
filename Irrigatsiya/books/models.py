from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify


class UserBooks(models.Model):
    name = models.CharField(max_length=500)
    file = models.FileField(blank=True, upload_to="Files")
    slug = models.SlugField(blank=False, null=False, unique=True, max_length=500)
    link = models.URLField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'UserBooks'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if  not self.slug :
            self.slug = slugify(self.name)
        return super(UserBooks, self).save(*args, **kwargs)

class Book(models.Model):
    name = models.CharField(max_length=500)   # name = models.CharField(max_length=200 ) #muqovasi
    file = models.FileField(blank=True, upload_to="Files")# book = models.FileField( blank=True, upload_to='books')# full_name = models.CharField(max_length=500)
    slug = models.SlugField(blank=False, null=False, unique=True, max_length=500)# slug = models.SlugField(max_length=200, null=False)
    link = models.URLField(blank=True, null=True)# link = models.URLField(blank=True, null=True,)
    author = models.ForeignKey(User, on_delete=models.CASCADE)# author = models.ForeignKey(User, on_delete = models.CASCADE)  
    pub_date = models.DateTimeField(auto_now_add=True)# pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)# up_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if  not self.slug :
            self.slug = slugify(self.name)
        return super(Book, self).save(*args, **kwargs)

        
    def get_absolute_url(self):
        return reverse('books')
    # class Meta:
    #     verbose_name_plural = 'Books'

    # def __str__(self):
    #     return self.name
    

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #         return super(Book, self).save(*args, **kwargs)

@receiver(pre_delete, sender=Book)
def object_file_delete(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete()

