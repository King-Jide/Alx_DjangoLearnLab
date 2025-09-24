#relationship_app/urls.py
from django.urls import path
from . import views
from .views import list_books

app_name = "relationship_app" #namespacing is good practice

urlpatterns = [
    #Function-based view route: list all books
    path("books/", views.list_books, name="list_books"),

    # Class-based view route: detail of a specific library by its pk
    #Example: /library/1/ for library with pk= 1
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
]
