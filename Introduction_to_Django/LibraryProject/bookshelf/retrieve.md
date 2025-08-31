
### `retrieve.md`
```markdown
# Retrieve Operation

```python
retrieved_book = Book.objects.get(id=book.id)
retrieved_book.title       # "1984"
retrieved_book.author      # "George Orwell"
retrieved_book.publication_year  # 1949
