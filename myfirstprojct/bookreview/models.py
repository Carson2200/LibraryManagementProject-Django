from django.db import models

# Create your models here.
class Author(models.Model):
    objects = models.Manager
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f'Author ({self.firstName}, {self.lastName}, {self.email})'

class Book(models.Model):
    objects = models.Manager
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
