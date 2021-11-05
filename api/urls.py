from django.urls import path
from rest_framework.urlpatterns import (
    format_suffix_patterns,
)
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from api.views import (
    BookListCreateAPIView,
    BookDetailAPIView,
    AuthorListCreateAPIView,
    AuthorDetailAPIView,
    api_root,
)

urlpatterns = format_suffix_patterns(
    [
        path("", api_root),
        path("schema/", get_schema_view(), name="openapi-schema"),
        path(
            "swagger-ui/",
            TemplateView.as_view(
                template_name="swagger-ui.html",
                extra_context={"schema_url": "openapi-schema"},
            ),
            name="swagger-ui",
        ),
        path("books/", BookListCreateAPIView.as_view(), name="book-list"),
        path("books/<int:pk>/", BookDetailAPIView.as_view(), name="book-detail"),
        path("authors/", AuthorListCreateAPIView.as_view(), name="author-list"),
        path("authors/<int:pk>/", AuthorDetailAPIView.as_view(), name="author-detail"),
    ]
)
