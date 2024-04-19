from uuid import uuid4

from django.db import models
from django.conf import settings


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    POlITICS = "P"
    FINANCE = "F"
    ROMANCE = "R"

    BOOK_CHOICES = [
        (POlITICS, 'politics'),
        (FINANCE, 'Finance'),
        (ROMANCE, 'Romance')
    ]
    title = models.CharField(max_length=255)
    summary = models.TextField()
    isbn = models.CharField(max_length=13)
    genre = models.ManyToManyField(Genre)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.isbn}"

    def list_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:2])


class Author(models.Model):
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Language(models.Model):
    name = models.CharField(max_length=255)


class BookInstance(models.Model):
    AVAILABLE = "A"
    UNAVAILABLE = "u"
    LOAN_CHOICES = [
        (AVAILABLE, "available"),
        (UNAVAILABLE, "unavailable")
    ]
    uniqueId = models.UUIDField(default=uuid4, primary_key=True)
    status = models.CharField(max_length=50, choices=LOAN_CHOICES, default=AVAILABLE)
    due_back = models.DateField()
    status = models.CharField(max_length=1, choices=LOAN_CHOICES, default=AVAILABLE)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    borrower = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return f"{self.status} {self.due_back} {self.borrower}"
