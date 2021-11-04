from books.models import Book, Author
from django.test import TestCase


class BookTest(TestCase):
    def setUp(self) -> None:
        self.a = Author.objects.create(name="Test Author")

    def test_create_book_should_return_correct_data(self):
        book: Book = Book.objects.create(
            title="My book", subtitle="My sub", author=self.a, isbn=12334
        )
        self.assertEqual(
            f"{book.title} - {book.subtitle} by {book.author}. ISBN: {book.isbn}",
            book.__str__(),
        )
