from django.contrib import admin
from .models import Videos

class VideosAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Videos, VideosAdmin)

