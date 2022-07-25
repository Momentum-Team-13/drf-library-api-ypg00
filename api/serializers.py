from rest_framework import serializers
from books.models import User, Book, TrackedBook, Note
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk',
            'username',
            'email',
            'password',
        ]

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'genre',
            'publication_date',
            'featured',
        ]

class TrackedBookSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = TrackedBook
        fields = [
            'user',
            'book',
            'status',
        ]

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = [
            'pk',
            'book',
            'title',
            'note',
            'public',
        ]
