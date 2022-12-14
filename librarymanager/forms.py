from django import forms

from librarymanager.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'author', 'year', 'numberPages', 'img')

class LastPageRead(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('lastPageRead', )