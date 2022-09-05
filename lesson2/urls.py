"""lesson2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.template.context_processors import request
from django.urls import path


def test(request):
    return HttpResponse(f'<h1>{test.__name__}</h1>')


def test_main(request):
    return HttpResponse(f'<h1>{test_main.__name__}</h1>')


def main_page_home_python(request):
    return HttpResponse(f'<h1>{main_page_home_python.__name__}</h1>')

def path_link(link):
    return f'{link}/'
def link(request):
    return HttpResponse(f'<h1><a href>127.0.0.1:8000/task2.3/</a><h1>')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test),
    path('test/main/', test_main),
    path('main_page/home/python/', main_page_home_python),
    path(path_link('task2.3'),link),
]
