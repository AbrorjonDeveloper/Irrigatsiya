from django.contrib import admin
from .models import Book, UserBooks

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('id','name', 'author', 'up_date', 'pub_date', )
    list_filter = ('up_date', 'pub_date')
    # ordering = ['-up_date', '-pub_date']

admin.site.register(UserBooks)
admin.site.register(Book, BookAdmin)
