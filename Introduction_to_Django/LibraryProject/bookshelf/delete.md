# 📘 Delete Operation

Delete the book instance and confirm it no longer exists.

```python
from bookshelf.models import Book

updated_book.delete()

Book.objects.all()
# Output: <QuerySet []>



