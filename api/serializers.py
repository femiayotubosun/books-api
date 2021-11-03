from rest_framework import fields, serializers
from books.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name"]


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer

    class Meta:
        model = Book
        fields = ["id", "title", "subtitle" "isbn"]
