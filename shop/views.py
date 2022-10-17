from django.shortcuts import HttpResponse,render
from shop.models import Book_shop
from shop.models import Book



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


def book_shop_show_sell(request):
    context = {
    }
    return render(request, 'book_shop_show.html', context)


def book_shop_update_sell(request):
    context = {
    }
    return render(request, 'book_shop_edite.html', context)


def book_shop_remove_sell(request):
    context = {
    }
    return render(request, 'book_shop_del.html', context)


def admin_page(requqest):
    return HttpResponse(f'<h1><a href= "http://127.0.0.1:8000/admin/">Link for admin part</a>.<h1>')

def base_page(requqest):
    context ={
    }
    return render(requqest, 'unit.html', context)
def shop_comics(requqest):
    queryset = Book_shop.objects.all()
    context ={
    'title':'Comics',
    'object_list':queryset,
    'filter' : 'комікси'
    }
    return render(requqest, 'book_shop_comics.html', context)
def shop_historical(requqest):
    queryset = Book_shop.objects.all()
    context ={
    'title':'Historical story',
    'object_list':queryset,
    'filter' : 'історична повість'
    }
    return render(requqest, 'book_shop_historical.html', context)

def shop_poems(requqest):
    queryset = Book_shop.objects.all()
    context ={
    'title':'Historical story',
    'object_list':queryset,
    'filter' : 'вірші'
    }
    return render(requqest, 'book_shop_poems.html', context)
