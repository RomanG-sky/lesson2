from django import forms
from shop.models import Author, Book, Book_shop, Genre


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'last_name',
            'first_name',
            'date_of_birth',
            'pic'
        ]


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'book_name',
            'book_language',
            'author',
            'genre',
            'year_of_issue',
            'isbn',
            'pic'
        ]


class GenreForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'genre'
        ]


class BookShopForm(forms.ModelForm):
    class Meta:
        model = Book_shop
        fields = [
            'book',
            'price',
            'currency',
            'quantity',
            'url',
            'booked',
            'sale'
        ]