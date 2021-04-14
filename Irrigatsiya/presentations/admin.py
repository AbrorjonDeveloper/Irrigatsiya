from django.contrib import admin
from .models import Presentations

class PresentationsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(Presentations, PresentationsAdmin)
