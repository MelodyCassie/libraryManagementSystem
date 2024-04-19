from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='books'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('authors/', views.author_list, name='authors'),
    path('author/<int:pk>', views.author_details, name='author_detail')
]
