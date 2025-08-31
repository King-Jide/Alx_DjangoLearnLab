# 📘 CRUD Operations with the Book Model

This document demonstrates the four basic CRUD operations (Create, Retrieve, Update, Delete) using Django’s ORM with the `Book` model inside the **bookshelf** app.

---

## 🔹 1. Create

Create a new `Book` instance with the title **"1984"**, author **"George Orwell"**, and publication year **1949**.

```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book
# Output: <Book: 1984 by George Orwell (1949)>
```

---

## 🔹 2. Retrieve

Retrieve the book we just created and display its attributes.

```python
retrieved_book = Book.objects.get(id=book.id)

retrieved_book.title
# Output: '1984'

retrieved_book.author
# Output: 'George Orwell'

retrieved_book.publication_year
# Output: 1949
```

---

## 🔹 3. Update

Update the book’s title from **"1984"** to **"Nineteen Eighty-Four"**.

```python
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()

updated_book = Book.objects.get(id=book.id)
updated_book.title
# Output: 'Nineteen Eighty-Four'
```

---

## 🔹 4. Delete

Delete the book instance and confirm it no longer exists.

```python
updated_book.delete()

Book.objects.all()
# Output: <QuerySet []>
```

---

✅ These steps confirm that the `Book` model in the **bookshelf** app supports all fundamental CRUD operations using Django’s ORM.
