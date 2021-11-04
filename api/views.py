from rest_framework import generics, serializers
from books.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer
from abc import ABC
from rest_framework.utils import json


class BaseBookAPIView(ABC):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListCreateAPIView(BaseBookAPIView, generics.ListCreateAPIView):
    pass


class BookDetailAPIView(BaseBookAPIView, generics.RetrieveAPIView):
    pass


class BaseAuthorView(ABC):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorListCreateAPIView(BaseAuthorView, generics.ListCreateAPIView):
    pass


class AuthorDetailAPIView(BaseAuthorView, generics.RetrieveAPIView):
    pass
