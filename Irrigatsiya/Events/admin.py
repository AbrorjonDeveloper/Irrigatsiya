from django.contrib import admin
from .models import Events

class EventsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    # ordering = ['-up_date', '-pub_date']

admin.site.register(Events,EventsAdmin)

