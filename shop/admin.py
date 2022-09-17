from django.contrib import admin
from shop.models import Author
from shop.models import Book_shop
from shop.models import Book




class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth')
    list_filter = ('last_name',)
    list_per_page = 20


class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'isbn', 'year_of_issue','genre','book_language','author')
    list_filter = ('book_name','genre','author')
    list_per_page = 20

class Book_shopAdmin(admin.ModelAdmin):
    list_display = ('book', 'price', 'currency','quantity','booked','sale')
    list_filter = ('sale','book','quantity','price')


admin.site.register(Author,AuthorAdmin)
admin.site.register(Book_shop,Book_shopAdmin)
admin.site.register(Book,BookAdmin)