from django.http import response
from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory
from books.models import Book, Author
from api.serializers import BookSerializer, AuthorSerializer
from rest_framework import status


class ApiTest(TestCase):
    def setUp(self):
        self.c = Client()

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
        pass

    def test_authors_route_should_return_empty_list(self):
        response = self.c.get("/api/authors/")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(0, len(response.data))

    def test_authors_route_data_should_return_4_authors(self):
        Author.objects.create(name="Test Author1")
        Author.objects.create(name="Test Author2")
        Author.objects.create(name="Test Author3")
        Author.objects.create(name="Test Author4")

        response = self.c.get("/api/authors/")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(4, len(response.data))

    def test_authors_route_create_author_should_add_new_author_to_db(self):
        authors = Author.objects.all().count()
        response = self.client.post("/api/authors/", {"name": "My author is a beast"})
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(authors + 1, Author.objects.all().count())


# Create your tests here.
