from django.urls import path
from api.views import (
    BookListCreateAPIView,
    BookDetailAPIView,
    AuthorListCreateAPIView,
    AuthorDetailAPIView,
)

urlpatterns = [
    path("", BookListCreateAPIView.as_view()),
    path("<int:pk>/", BookDetailAPIView.as_view()),
    path("authors/", AuthorListCreateAPIView.as_view()),
    path("authors/<int:pk>/", AuthorDetailAPIView.as_view()),
]
