from django.contrib import admin

from .models import Authors, Books


class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'country', 'updated_at')
    list_display_link = ('id', 'full_name')
    filter_horizontal = ['books']
    search_fields = ['full_name', 'country']
    

class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'updated_at')
    list_display_link = ('id', 'title')
    search_fields = ['title']


admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Books, BooksAdmin)
