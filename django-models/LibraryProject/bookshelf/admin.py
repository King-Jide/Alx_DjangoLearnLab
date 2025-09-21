from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    #Columns shown in the list view
    list_display = ('title', 'author', 'publication_year')
    
    #Add Filters in the right sidebar
    list_filter = ('author', 'publication_year')
    
    #Add a search bar
    search_fields = ('title', 'author')
    
#Register with custom settings
admin.site.register(Book, BookAdmin)
