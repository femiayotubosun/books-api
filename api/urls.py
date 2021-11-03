from django.urls import path
from api.views import AuthorListCreateAPIView, BookListCreateAPIView

urlpatterns = [
    path("books/", BookListCreateAPIView.as_view()),
    path("authors/", AuthorListCreateAPIView.as_view()),
]
