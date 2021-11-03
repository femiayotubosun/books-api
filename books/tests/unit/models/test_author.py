from django.test import TestCase
from books.models import Author


class AuthorTest(TestCase):
    def setUp(self):
        pass

    def test_create_author_should_return_correct_data(self) -> None:
        test_author: Author = Author.objects.create(name="Test Author")
        self.assertEqual(
            test_author.name,
            "Test Author",
            f"Set name did not match the returned name. Expected 'Test Author' got '{test_author.name}'",
        )

        self.assertEqual("Test Author", test_author.__repr__())
