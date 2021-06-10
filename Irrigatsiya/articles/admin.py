from django.contrib import admin
from .models import Articles

class ArticlesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('id', 'name', 'file', 'author', 'up_date')
    list_filter = ('pub_date', 'up_date')

admin.site.register(Articles, ArticlesAdmin)

