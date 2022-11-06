from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, render, get_object_or_404,HttpResponseRedirect
from shop.models import Book_shop,Book,Genre,Author
from shop.forms import AuthorForm,BookForm,GenreForm,BookShopForm



def book_add(request):
    form = BookForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/shop/books/')

    context = {
        'title': 'BOOK CREATE ',
        'form': form

    }
    return render(request, 'book_add.html', context)


def books(request):
    queryset = Book_shop.objects.all()
    context ={
    'title':'Book shop',
    'object_list':queryset,
    'filter': 0
    }
    return render(request, 'book_shop_books.html',context)

def book_update(request):
    context = {
    }
    return render(request, 'book_edite.html')


def book_remove(request):
    context = {
    }
    return render(request, 'book_del.html', context)


def author_add(request):
    form = AuthorForm(request.POST  or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/shop/author/')


    context = {
        'title': 'AUTHOR CREATE ',
        'form': form

    }
    return render(request, 'author_add.html',context)


def author(request):
    queryset = Author.objects.all()
    queryset2 = Book_shop.objects.all()
    context = {
        'title': 'Book shop',
        'object_list': queryset,
        'object_list2': queryset2

    }
    return render(request, 'book_shop_author.html', context)

def author_show(request):
    instance = get_object_or_404(Author,first_name ='first_name', last_name = 'last_name')
    context = {
        'title' : 'Book detail',
        'object' : instance
        }
    return render(request, 'book_shop_base_categories.html', context)

def author_update(request):
    context = {
    }
    return render(request, 'author_edite.html', context)


def author_remove(request):
    context = {
    }
    return render(request, 'author_del.html')


def book_shop_add(request):
    form = BookShopForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/shop/')

    context = {
        'title': 'CREATE BOOK ',
        'form': form

    }
    return render(request, 'book_shop_add.html', context)



def book_shop_edite(request):

    form = BookShopForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/shop/')

    context = {
        'title': 'CREATE BOOK ',
        'form': form

    }
    return render(request, 'book_shop_add.html', context)



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
    return render(requqest, 'book_shop_sale.html', context)

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

def genre(request):
    queryset = Genre.values
    context ={
    'title':'Book shop',
    'object_list':queryset
    }
    return render(request, 'book_shop_genre.html', context)

def genre_add(request):
    form = GenreForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/shop/genre/')

    context = {
        'title': 'CREATE GENRE ',
        'form': form

    }
    return render(request, 'book_shop_add.html', context)
