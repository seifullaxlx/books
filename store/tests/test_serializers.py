from unittest import TestCase

from django.contrib.auth.models import User

from store.models import Book
from store.serializers import BooksSerializer


class BookSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_ok_username',)
        self.book_1 = Book.objects.create(name='Test book 1', price=25, author_name='Author 1',
                                          owner=self.user)
        self.book_2 = Book.objects.create(name='Test book 2', price=55, author_name='Author 2',
                                          owner=self.user)

    def test_ok(self):
        data = BooksSerializer([self.book_1, self.book_2], many=True).data
        expected_data = [
            {
                'id': self.book_1.id,
                'name': 'Test book 1',
                'price': '25.00',
                'author_name': 'Author 1'
            },
            {
                'id': self.book_2.id,
                'name': 'Test book 2',
                'price': '55.00',
                'author_name': 'Author 2'
            },
        ]
        self.assertEqual(expected_data, data)
