from django.shortcuts import render, ger_objeect_or_404
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library

#-----------------------------------
#Function-based view: list all books
#-----------------------------------
def list_books(request):
    """
    List all books in the database. Renders an HTML template with books context.
    Uses select_related('author) tio avoid N+1 query when accessing book.author
    """
    #QuerySet of all books; use select_related to fetch author in the same query
    books = Book.object.select_related('author').all()

    #if you prefer plain text instead of template, uncomment the next block:
    #lines = [f"{b.title} by {b.author.name}" for b in books]
    # return HttpResponse("\n".join(lines), content_type="text/plain")

    # Render the HTML template with books available under the "books" context variable
    return render(request, "relationship_app/list_books.html", {"books":books})
# Create your views here.

#------------------------------------------------------
# Class-based view: Detail of a specific library (book inside)
#------------------------------------------------------
class LibraryDetailView(DetailView):
    """"
    Detail view for a specific library, showing its books.
    Uses prefetch_related to optimize ManyToMany access to books.
    """
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_queryset(self):
        """
        Optimize DB access by prefetching the ManyToMany related books and their authors.
        """
        #Override get_queryset to prefetch related books to avoid N+1 queries
        return super().get_queryset().prefetch_related('books__author')
    
