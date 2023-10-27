from django.urls import path
from book.views import get_books
app_name = 'booklist'

urlpatterns = [
    path("api/book/", get_books, name="get_books"),
]