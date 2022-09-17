from django.shortcuts import HttpResponse



def book_add(request):
    return HttpResponse('<h1>book add</h1>')

def book_show(request):
    return HttpResponse('<h1>show book</h1>')

def book_update(request):
    return HttpResponse('<h1>book update</h1>')

def book_remove(request):
    return HttpResponse('<h1>book remove</h1>')

def author_add(request):
    return HttpResponse('<h1>author add</h1>')

def author_show(request):
    return HttpResponse('<h1>author book</h1>')

def author_update(request):
    return HttpResponse('<h1>author update</h1>')

def author_remove(request):
    return HttpResponse('<h1>author_remove</h1>')

def book_shop_add_sell(request):
    return HttpResponse('<h1>author add sell position</h1>')

def book_shop_show_sell(request):
    return HttpResponse('<h1>author book sell position</h1>')

def book_shop_update_sell(request):
    return HttpResponse('<h1>author update sell position</h1>')

def book_shop_remove_sell(request):
    return HttpResponse('<h1>shop remove sell position</h1>')
def admin_page(requqest):
    return HttpResponse(f'<h1><a href= "http://127.0.0.1:8000/admin/">Link for admin part</a>.<h1>')
