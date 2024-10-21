from django.urls import path
from .views import RegisterView, BookListCreateView, ReviewCreateView, BookReviewsListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('books/', BookListCreateView.as_view(), name='books_list_create'),
    path('books/<int:book_id>/reviews/', ReviewCreateView.as_view(), name='book_review_create'),
    path('books/<int:book_id>/reviews/list/', BookReviewsListView.as_view(), name='book_review_list'),
]
