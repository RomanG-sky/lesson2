from django.urls import path
from shop import views

urlpatterns = [
    path('',views.admin_page),
    path('author/add/',views.author_add),
    path('book/add/',views.book_add),
    path('book_shop/add',views.book_shop_add_sell)
    # Add only links for add parts
]