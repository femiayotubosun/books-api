from django.test import TestCase
from unittest import skip
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient
from books.models import Book, Author
from api.serializers import BookSerializer, AuthorSerializer
from api.views import BookDetailAPIView, BookListCreateAPIView


class ApiTest(TestCase):
    def setUp(self):
        self.c = APIClient()
        self.factory = APIRequestFactory()
        self.author = Author.objects.create(name="Test Author")
        self.author_serializer = AuthorSerializer(self.author)

    def test_authors_route_should_return_list_with_one_data(self):
        response = self.c.get("/api/authors/")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, len(response.data))

    def test_authors_route_data_should_return_4_authors(self):
        Author.objects.create(name="Test Author1")
        Author.objects.create(name="Test Author2")
        Author.objects.create(name="Test Author3")
        Author.objects.create(name="Test Author4")

        response = self.c.get("/api/authors/")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(5, len(response.data))

    def test_authors_route_create_author_should_add_new_author_to_db(self):
        authors = Author.objects.all().count()
        response = self.client.post("/api/authors/", {"name": "My author is a beast"})
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(authors + 1, Author.objects.all().count())

    def test_home_page_should_return_empty_list_with_200(self):

        response = self.c.get("/api/")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(len(response.data), 0)

    def test_home_page_with_data_should_return_list_of_4_dicts(self):
        a = Author.objects.create(name="Test Author")
        Book.objects.create(
            title="Test Title 1", subtitle="A book", author=a, isbn=1234
        )
        Book.objects.create(
            title="Test Title 2", subtitle="A book3", author=a, isbn=12344
        )
        Book.objects.create(
            title="Test Title 3", subtitle="A book", author=a, isbn=1234322
        )
        Book.objects.create(
            title="Test Title 4", subtitle="A book", author=a, isbn=1234121
        )
        response = self.c.get("/api/")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(4, len(response.data))

    def test_home_page_create_new_book_should_add_book_to_db(self):
        # response = self.client.post("/api/authors/", {"name": "My author is a beast"})
        # self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        payload = {
            "author": self.author_serializer.data,
            "title": "John Wick",
            "subtitle": "Where has my dog gone?",
            "isbn": 123441,
        }

        books_count = Book.objects.all().count()
        request = self.factory.post("/api/", payload, format="json")
        response = BookListCreateAPIView.as_view()(request)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(books_count + 1, Book.objects.all().count())

    def test_create_new_book_invalid_author_should_return_400_no_book_added(self):
        payload = {
            "author": {"name": "dd"},
            "title": "Test book",
            "subtitle": "Test subtitile",
            "isbn": 1234,
        }
        books_count = Book.objects.all().count()
        request = self.factory.post("/api/", payload, format="json")
        response = BookListCreateAPIView.as_view()(request)
        response.render()
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertDictEqual({"author": "This author does not exist."}, response.data)
        self.assertEqual(books_count, Book.objects.all().count())

    def test_update_book_valid_data_should_return_200(self):
        book = Book.objects.create(
            title="Test title", subtitle="Test sub", author=self.author, isbn=1234
        )

        payload = {
            "title": "Test title -- updated",
            "subtitle": "Test sub",
            "author": {"name": "Test Author"},
            "isbn": 1234,
        }

        request = self.factory.patch(f"/api/{book.pk}/", payload, format="json")
        response = BookDetailAPIView.as_view()(request, pk=1)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        response.render()
        book = Book.objects.all().first()
        self.assertEqual(book.title, payload["title"])

    def test_update_book_invalid_data_should_return_400(self):
        book = Book.objects.create(
            title="Test title", subtitle="Test sub", author=self.author, isbn=1234
        )

        payload = {
            "title": "Test title",
            "subtitle": "Test sub",
            "author": {"name": "Test Ar"},
            "isbn": 1234,
        }

        request = self.factory.patch(f"/api/{book.pk}/", payload, format="json")
        response = BookDetailAPIView.as_view()(request, pk=1)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)


# Create your tests here.
