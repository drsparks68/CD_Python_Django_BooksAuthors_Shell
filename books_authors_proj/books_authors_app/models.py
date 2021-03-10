from django.db import models

class books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(default = {title})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __repr__(self):
        return f"<Book: {self.title}>"


class authors(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    books = models.ManyToManyField(books, related_name="authors")
    notes = models.TextField(default = "A Book")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Author: {self.first_name} {self.last_name}>"


