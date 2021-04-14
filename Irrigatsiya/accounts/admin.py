from django.contrib import admin
from .models import  Profile, Faculty, Cafedra, Level

class ProfileAdmin(admin.ModelAdmin):
    # list_display = ( 'faculty', 'cafedra', 'level')
    pass

admin.site.register(Faculty)
admin.site.register(Cafedra)
admin.site.register(Level)
admin.site.register(Profile, ProfileAdmin)
