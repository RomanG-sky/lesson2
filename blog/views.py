from django.shortcuts import HttpResponse
from lesson2 import task_4


def book_add(request):
    return HttpResponse('<h1>book add</h1>')

def book_show(request):
    return HttpResponse('<h1>show book</h1>')

def book_update(request):
    return HttpResponse('<h1>book_update</h1>')

def book_remove(request):
    return HttpResponse('<h1>book_remove</h1>')
