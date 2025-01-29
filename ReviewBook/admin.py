from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at','average_rating','number_of_reviews','isbn','publication_date')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    # list_editable = ('average_rating', 'number_of_reviews')
    


admin.site.register(Book, BookAdmin)