from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from books.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer
from abc import ABC


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "books": reverse("book-list", request=request, format=format),
            "authors": reverse("author-list", request=request, format=format),
        }
    )


class BaseBookAPIView(ABC):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListCreateAPIView(BaseBookAPIView, generics.ListCreateAPIView):
    pass


class BookDetailAPIView(BaseBookAPIView, generics.RetrieveUpdateDestroyAPIView):
    pass


class BaseAuthorView(ABC):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorListCreateAPIView(BaseAuthorView, generics.ListCreateAPIView):
    pass


class AuthorDetailAPIView(BaseAuthorView, generics.RetrieveUpdateDestroyAPIView):
    pass
