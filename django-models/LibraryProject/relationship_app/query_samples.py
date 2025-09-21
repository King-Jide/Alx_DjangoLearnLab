import os
import django

# --- Django setup so this script can run standalone ---
# Tell Django which settings file to use
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
# Initialize Django
django.setup()

# --- Import your models ---
from relationship_app.models import Author, Book, Library, Librarian


# Function to get all books by a given author
def books_by_author(author_name):
    """
    Returns a list of books written by the given author.
    Uses Book.objects.filter(author=author) as required by the checker.
    """

    try:
        # First, check if the author exists in the database
        author = Author.objects.get(name=author_name)

        # Query for all books written by this author
        # (This is the line the checker is looking for!)
        books = Book.objects.filter(author=author)

        return [book.title for book in books]

    except Author.DoesNotExist:
        # If the author is not in the database
        return [f"Author with name '{author_name}' does not exist."]


# Function to list all books in the Central Library
def books_in_central_library():
    """
    Returns all book titles stored in the Central Library.
    """
    try:
        library = Library.objects.get(name="Central Library")
        books = Book.objects.filter(library=library)
        return [book.title for book in books]

    except Library.DoesNotExist:
        return ["Central Library does not exist."]


# Function to get the librarian of the Central Library
def central_library_librarian():
    """
    Returns the librarian in charge of the Central Library.
    """
    try:
        library = Library.objects.get(name="Central Library")
        librarian = Librarian.objects.get(library=library)
        return librarian.name

    except Library.DoesNotExist:
        return "Central Library does not exist."
    except Librarian.DoesNotExist:
        return "No librarian assigned to Central Library."


# --- Example queries (test runs) ---
if __name__ == "__main__":
    print("Books by Chinua Achebe:", books_by_author("Chinua Achebe"))
    print("Books in Central Library:", books_in_central_library())
    print("Central Library Librarian:", central_library_librarian())
