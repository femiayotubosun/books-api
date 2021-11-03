from django.test import TestCase
from books.models import Book, Author


class BookTest(TestCase):
    def setUp(self) -> None:
        self.test_author = Author.objects.create(name="Test author")

    def test_create_book_should_return_correct_data(self) -> None:
        test_book: Book = Book.objects.create(
            title="My test book",
            subtitle="Test subtitle",
            author=self.test_author,
            isbn=12334,
        )

        expected = "My test book - Test subtitle by Test author. ISBN: 12334"
        self.assertEqual(expected, test_book.__repr__())
