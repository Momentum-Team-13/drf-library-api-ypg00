from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from books.models import User, Book, TrackedBook, Note
from api.serializers import UserSerializer, BookSerializer, TrackedBookSerializer

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = ['author', 'title']

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

# Admin only
class BookRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [permissions.IsAdminUser]

class TrackedBookListCreate(ListCreateAPIView):
    queryset = TrackedBook.objects.prefetch_related('book')
    serializer_class = TrackedBookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
