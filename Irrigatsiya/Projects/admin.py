from django.contrib import admin
from .models import Projects

class ProjectsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}


admin.site.register(Projects, ProjectsAdmin)

