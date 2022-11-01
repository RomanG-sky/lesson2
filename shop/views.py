from django.shortcuts import HttpResponse, render, get_object_or_404
from shop.models import Book_shop
from shop.models import Book
from shop.models import Genre



def book_add(request):
    context ={
    }
    return render(request, 'book_add.html')

def book_show(request):
    context = {
    }
    return render(request, 'book_show.html')

def book_update(request):
    context = {
    }
    return render(request, 'book_edite.html')


def book_remove(request):
    context = {
    }
    return render(request, 'book_del.html', context)


def author_add(request):
    return render(request, 'author_add.html')


def author_show(request):
    context = {
    }
    return render(request, 'author_show.html', context)


def author_update(request):
    context = {
    }
    return render(request, 'author_edite.html', context)


def author_remove(request):
    context = {
    }
    return render(request, 'author_del.html')


def book_shop_add_sell(request):
    context = {
    }
    return render(request, 'book_shop_add.html')





def book_shop_update_sell(request):
    context = {
    }
    return render(request, 'book_shop_edite.html', context)



def admin_page(requqest):
    return HttpResponse(f'<h1><a href= "http://127.0.0.1:8000/admin/">Link for admin part</a>.<h1>')

def base(requqest):
    queryset = Book_shop.objects.all()
    context ={
    'title':'Book shop',
    'object_list':queryset,
    'filter': 0
    }
    return render(requqest, 'book_shop_base.html', context)

def shop_sale(requqest):
    queryset = Book_shop.objects.all()
    context ={
    'title':'Book shop',
    'object_list':queryset,
    'filter': True
    }
    return render(requqest, 'book_shop_base.html', context)

def book_shop_show(request, id=None):
    instance = get_object_or_404(Book_shop,id=id)
    context = {
        'title' : 'Book detail',
        'object' : instance
        }
    return render(request, 'book_shop_show_book.html', context)
def shop_comics(requqest):
    queryset = Book_shop.objects.all()
    context ={
    'title':'Comics',
    'object_list':queryset,
    'filter' : 'comics'
    }
    return render(requqest, 'book_shop_base_categories.html', context)
def shop_historical(requqest):
    queryset = Book_shop.objects.all()
    context ={
    'title':'Historical story',
    'object_list':queryset,
    'filter' : 'historical'
    }
    return render(requqest, 'book_shop_base_categories.html', context)

def shop_poems(requqest):
    queryset = Book_shop.objects.all()
    context ={
    'title':'Poems',
    'object_list':queryset,
    'filter' : 'poems'
    }
    return render(requqest, 'book_shop_base_categories.html', context)

def shop_genre(request):
    queryset2 = Genre.values
    queryset = Genre.names
    context ={
    'title':'Book shop',
    'object_list':queryset,
    'object_list_genre':queryset2
    }
    return render(request, 'book_shop_genre.html', context)
