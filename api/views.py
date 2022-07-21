from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from books.models import User, Book, TrackedBook, Note
from .serializers import UserSerializer, BookSerializer

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
