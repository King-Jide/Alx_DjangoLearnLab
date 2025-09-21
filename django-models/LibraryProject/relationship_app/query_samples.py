import sys
import os 
import django

# add the project root to sys.path
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

#Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# ---Sample Queries---

#1. All Books by a Specific Author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()
    except Author.DoesNotExist:
        return f"No author found with name '{author_name}'."

    

#2. All books in a Library

def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return None
    
#3. The librarian for a library
def librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        return librarian
    except Library.DoesNotExist:
        return None
    except Librarian.DoesNotExist:
        return None
    

if __name__ == "__main__":
    print(books_by_author("Chinua Achebe"))
    print(books_in_library("Central Library"))
    print(librarian_of_library("Central Library"))
    print(librarian_of_library("Nonexistent Library"))
    print(books_by_author("Nonexistent Author"))
    print(books_in_library("Nonexistent Library"))


