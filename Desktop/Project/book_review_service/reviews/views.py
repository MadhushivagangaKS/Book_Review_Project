from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Book, Review
from .serializers import RegisterSerializer, BookSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

# Register View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Login view
from rest_framework_simplejwt.views import TokenObtainPairView

# Book List and Creation View
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Review Creation View
class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        book = Book.objects.get(id=self.kwargs['book_id'])
        serializer.save(user=self.request.user, book=book)

# Book Reviews List View
class BookReviewsListView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        book = Book.objects.get(id=self.kwargs['book_id'])
        return Review.objects.filter(book=book)
