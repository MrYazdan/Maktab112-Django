from django.contrib import admin
from .models import Profile, Author, Book, Category, Reader


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'cover_image', 'is_available')
    list_display_links = ('id', 'title')
    list_filter = ('is_available',)
    search_fields = ('title',)
    search_help_text = "Search based on the name of the book ..."
    readonly_fields = ('is_available',)


admin.site.register(Book, BookAdmin)
admin.site.register((Profile, Author, Category, Reader))
