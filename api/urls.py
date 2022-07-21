from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from api import views as api_views

urlpatterns = [
    path('register/', api_views.UserCreateView.as_view(), name='register'),
    path('books/', api_views.BookListCreateView.as_view(), name='book_list'),
]