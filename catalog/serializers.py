from rest_framework import serializers

from catalog.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class BookSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        queryset=Author.objects.all(),
        view_name='author_detail'
    )

    class Meta:
        model = Book
        fields = ['title', 'summary', 'isbn', 'author']
