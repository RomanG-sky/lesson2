from django.urls import path
from blog.views import book_add

urlpatterns = [
    path('', book_add),
]