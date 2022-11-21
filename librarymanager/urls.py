from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('livros', views.books, name='books'),
    path('livro/<int:book_id>', views.book_details, name='book_details'),
    path('novolivro/', views.new_book, name='new_book'),
    path('editar/<int:book_id>', views.edit_book, name='edit_book'),
    path('apagar/<int:book_id>', views.delete_book, name='delete_book')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)