from uuid import uuid4

from django.db import models
from django.conf import settings


# Create your models here.

class Book(models.Model):
    POLITICS = 'P'
    FINANCE = 'F'
    ROMANCE = 'R'
    BOOK_CHOICES = [
        ('POLITICS', 'politics'),
        ('FINANCE', 'Finance'),
        ('ROMANCE', 'Romance'),
    ]
    title = models.TextField(max_length=255)
    summary = models.TextField()
    isbn = models.CharField(max_length=10)
    genre = models.CharField(max_length=1, choices=BOOK_CHOICES, default='F')

    def __str__(self):
        return f"{self: name}"


class Author(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.CharField(null=True, blank=True)
    date_of_death = models.DateField(blank=True, null=True)


class Language(models.Model):
    name = models.CharField(max_length=255)


class BookInstance(models.Model):
    AVAILABLE = "A"
    UNAVAILABLE = "u"
    LOAN_CHOICES = [
        (AVAILABLE, "available")
        (UNAVAILABLE, "unavailable")
    ]
    uniqueId = models.UUIDField(default=uuid4, primary_key=True)
    status = models.CharField(max_length=1, choices=LOAN_CHOICES, default=AVAILABLE)
    due_back = models.DateField()
