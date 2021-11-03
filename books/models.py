from django.db import models

# Create your models here.
class Author(models.Model):
    name: str = models.CharField(max_length=80)

    def __repr__(self) -> str:
        return self.name

    def __str__(self):
        return self.name


class Book(models.Model):
    title: str = models.CharField(max_length=60)
    subtitle: str = models.CharField(max_length=60)
    author: Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn: int = models.IntegerField()

    def __repr__(self) -> str:
        return f"{self.title} - {self.subtitle} by {self.author}. ISBN: {self.isbn}"

    def __str__(self) -> str:
        return f"{self.title} - {self.subtitle} by {self.author}. ISBN: {self.isbn}"
