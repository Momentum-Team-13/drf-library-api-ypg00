from rest_framework import serializers
from books.models import User, Book, TrackedBook, Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'email',
            'password',
        )

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'title',
            'author',
            'genre',
            'publication_date',
            'featured',
        )
