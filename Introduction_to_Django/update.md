
### `update.md`
```markdown
# Update Operation

```python
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()

updated_book = Book.objects.get(id=book.id)
updated_book.title
# Output: "Nineteen Eighty-Four"
