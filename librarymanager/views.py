import random

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from librarymanager.models import Book
from librarymanager.forms import BookForm
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    return render(request, "home.html")

@login_required()
def books(request):
    search = request.GET.get('busca')

    if search:
        books = Book.objects.filter(name__icontains=search)
    else:
        books_list = Book.objects.all().order_by('-created_at')
        paginator = Paginator(books_list, 4)
        page = request.GET.get('page')
        books = paginator.get_page(page)

    context = {'books': books}
    return render(request, "books.html", context)

@login_required()
def book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book}
    return render(request, "book_details.html", context)

@login_required()
def new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            book = form.save(commit=False)
            book.lastPageRead = 0
            book.save()
            messages.success(request, 'Livro adicionado com sucesso.')
            return redirect('/livros')
        else:
            messages.warning(request, 'Ocorreu algum erro ao adicionar o livro.')
            return redirect('/livros')

        return render(request, "home.html")
    else:
        form = BookForm()
        context = {'form': form}
        return render(request, "new_book.html", context)

@login_required()
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = BookForm(instance=book)

    if (request.method == 'POST'):
        form = BookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            book.save()
            return redirect('/livros')
        else:
            return render(request, "edit_book.html", {'form': form, 'book': book})
    else:
        return render(request, "edit_book.html", {'form': form, 'book': book})

@login_required()
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    messages.success(request, 'Livro excluído com sucesso.')
    return redirect('/livros')
