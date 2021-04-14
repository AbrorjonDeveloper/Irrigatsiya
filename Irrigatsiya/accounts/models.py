from django.db import models
from django.contrib.auth.models import User
from PIL import Image
class Faculty(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Faculties'
    def __str__(self):
        return self.name

class Cafedra(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Cafedras'
    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = 'Academical Levels'
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    cafedra = models.ForeignKey(Cafedra, on_delete=models.SET_NULL, null=True)
    level = models.ForeignKey(Level, on_delete= models.SET_NULL, null=True)
    avatar = models.ImageField(default="download.jpg", upload_to="profile_pics")

    def __str__(self):
        return f'{self.user.username}\'s Profile' 

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.avatar.path) 

        if img.width>300 or img.height>300:
            output=(300, 300)
            img.thumbnail(output)
            img.save(self.avatar.path)
