from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, render, get_object_or_404, HttpResponseRedirect
from shop.models import Book_shop, Book, Genre, Author
from shop.forms import AuthorForm, BookForm, GenreForm, BookShopForm
from django.contrib import messages


def book_shop_list(requqest):
    queryset = Book_shop.objects.all()
    context = {
        'title': 'Book shop',
        'object_list': queryset,
        'filter': 0
    }
    return render(requqest, 'base.html', context)


def book_shop_detail(request, id=None):
    instance = get_object_or_404(Book_shop, id=id)
    context = {
        'title': 'Book detail',
        'title2': 'Book Shop',
        'object': instance,
    }
    return render(request, 'shop_detail.html', context)


def book_shop_create(request):
    form = BookShopForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Information successful updated!'
                                  '<br>''<br>'
                                  '<button class="btn"> <a class = "link_undecor" href =http://127.0.0.1:8000/shop/author/add/> Add new author </a></button>'
                                  '<br>' '<br>'
                                  '<button class="btn"><a class = "link_undecor" href =http://127.0.0.1:8000/shop/genre/> Book category </a> </button>'
                                  '<br>''<br>'
                                  '<button class="btn"><a  class = "link_undecor" href =http://127.0.0.1:8000/shop/add/> Add book </a></button>'

                         )
        return HttpResponseRedirect(instance.get_absolut_url())
    context = {
        'title': 'BOOK SHOP ',
        'title2': 'CREATE',
        'form': form

    }
    return render(request, 'shop_add.html', context)


def book_shop_update(request, id=None):
    instance = get_object_or_404(Book_shop, id=id)
    form = BookShopForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Information successful updated!'
                                  '<br>''<br>'
                                  '<button class="btn"> <a class = "link_undecor" href =http://127.0.0.1:8000/shop/author/add/> Add new author </a></button>'
                                  '<br>' '<br>'
                                  '<button class="btn"><a class = "link_undecor" href =http://127.0.0.1:8000/shop/genre/> Book category </a> </button>'
                                  '<br>''<br>'
                                  '<button class="btn"><a  class = "link_undecor" href =http://127.0.0.1:8000/shop/add/> Add book </a></button>'

                         )
        return HttpResponseRedirect(instance.get_absolut_url())

    context = {
        'title': 'BOOK EDITE ',
        'form': form

    }
    return render(request, 'shop_add.html', context)


def book_list(request):
    queryset = Book.objects.all()
    context = {
        'title': 'Book',
        'object_list': queryset,
    }
    return render(request, 'book_show.html', context)


def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Information successful updated!'
                                  '<br>''<br>'
                                  '<button class="btn"> <a class = "link_undecor" href =http://127.0.0.1:8000/shop/author/add/> Add new author </a></button>'
                                  '<br>' '<br>'
                                  '<button class="btn"><a class = "link_undecor" href =http://127.0.0.1:8000/shop/genre/> Book category </a> </button>'
                                  '<br>''<br>'
                                  '<button class="btn"><a  class = "link_undecor" href =http://127.0.0.1:8000/shop/add/> Add book </a></button>'

                         )
        return HttpResponseRedirect(instance.get_absolut_url_book())

    context = {
        'title': 'BOOK',
        'title2': 'CREATE',
        'form': form

    }
    return render(request, 'book_add.html', context)


def book_detail(request, id=None):
    instance = get_object_or_404(Book, id=id)
    context = {
        'title': 'Book detail',
        'object': instance,
    }
    return render(request, 'book_detail.html', context)


def book_update(request, id=None):
    instance = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Information successful updated!'
                                  '<br>''<br>'
                                  '<button class="btn"> <a class = "link_undecor" href =http://127.0.0.1:8000/shop/author/add/> Add new author </a></button>'
                                  '<br>' '<br>'
                                  '<button class="btn"><a class = "link_undecor" href =http://127.0.0.1:8000/shop/genre/> Book category </a> </button>'
                                  '<br>''<br>'
                                  '<button class="btn"><a  class = "link_undecor" href =http://127.0.0.1:8000/shop/add/> Add book </a></button>'

                         )
        return HttpResponseRedirect(instance.get_absolut_url_book())

    context = {
        'title': 'BOOK',
        'title2': 'UPDATE',
        'form': form

    }
    return render(request, 'book_add.html', context)


def book_remove(request):
    context = {
    }
    return render(request, 'book_del.html', context)


def author_list(request):
    queryset = Author.objects.all()
    queryset2 = Book_shop.objects.all()
    context = {
        'title': 'Author',
        'object_list': queryset,
        'object_list2': queryset2

    }
    return render(request, 'author_list.html', context)


def author_create(request):
    form = AuthorForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Information successful updated!'
                                  '<br>''<br>'
                                  '<button class="btn"> <a class = "link_undecor" href =http://127.0.0.1:8000/shop/author/add/> Add new author </a></button>'
                                  '<br>' '<br>'
                                  '<button class="btn"><a class = "link_undecor" href =http://127.0.0.1:8000/shop/genre/> Book category </a> </button>'
                                  '<br>''<br>'
                                  '<button class="btn"><a  class = "link_undecor" href =http://127.0.0.1:8000/shop/add/> Add book </a></button>'

                         )
        return HttpResponseRedirect(instance.get_absolut_url_author())


    context = {
        'title': 'AUTHOR ',
        'title2': 'CREATE',
        'form': form

    }
    return render(request, 'author_add.html', context)


def author_detail(request, id=None):
    instance = get_object_or_404(Author, id=id)
    queryset = Book_shop.objects.all()
    context = {
        'title': 'Author',
        'object': instance,
        'book': queryset
    }
    return render(request, 'author_detail.html', context)


def author_update(request, id=None):
    instance = get_object_or_404(Author, id=id)
    form = AuthorForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Information successful updated!'
                                  '<br>''<br>'
                                  '<button class="btn"> <a class = "link_undecor" href =http://127.0.0.1:8000/shop/author/add/> Add new author </a></button>'
                                  '<br>' '<br>'
                                  '<button class="btn"><a class = "link_undecor" href =http://127.0.0.1:8000/shop/genre/> Book category </a> </button>'
                                  '<br>''<br>'
                                  '<button class="btn"><a  class = "link_undecor" href =http://127.0.0.1:8000/shop/add/> Add book </a></button>'

                         )
        return HttpResponseRedirect(instance.get_absolut_url_author())

    context = {

        'title': 'AUTHOR ',
        'title2': 'EDITE',
        'form': form

    }
    return render(request, 'author_add.html', context)


def author_remove(request):
    context = {
    }
    return render(request, 'author_del.html')


def admin_page(requqest):
    return HttpResponse(f'<h1><a href= "http://127.0.0.1:8000/admin/">Link for admin part</a>.<h1>')


def shop_sale(requqest):
    queryset = Book_shop.objects.all()
    context = {
        'title': 'Book shop',
        'object_list': queryset,
        'filter': True
    }
    return render(requqest, 'sale_list.html', context)


def genre_list(request):
    queryset = Genre.values
    queryset2 = Book_shop.objects.all()
    context = {
        'title': 'Book shop',
        'object_list': queryset,
        'books': queryset2
    }
    return render(request, 'genre_list.html', context)


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
    return render(request, 'shop_add.html', context)


def genre_detail(request, id=None):
    instance = get_object_or_404(Genre, id=id)
    queryset = Book_shop.objects.all()
    context = {
        'title': 'Books for genre',
        'object': instance,
        'books': queryset
    }
    return render(request, 'genre_detail.html', context)
