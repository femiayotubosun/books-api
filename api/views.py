from rest_framework import generics, serializers
from books.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer
from abc import ABC
from rest_framework.utils import json


class BaseBookAPIView(ABC):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListCreateAPIView(BaseBookAPIView, generics.ListCreateAPIView):
    def perform_create(self, serializer):
        print(serializer.validated_data["author"])
        author = Author.objects.get(name=serializer.validated_data["author"]["name"])
        serializer.save(author=author)


class BookDetailAPIView(BaseBookAPIView, generics.RetrieveUpdateDestroyAPIView):
    pass


class BaseAuthorView(ABC):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorListCreateAPIView(BaseAuthorView, generics.ListCreateAPIView):
    pass


class AuthorDetailAPIView(BaseAuthorView, generics.RetrieveUpdateDestroyAPIView):
    pass
