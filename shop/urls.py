from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.book_shop_list, name = 'book_shop_list'),
    path('add/', views.book_shop_create),
    path('show/<int:id>', views.book_shop_detail),
    path('edite/<int:id>', views.book_shop_update),
    path('delete/<int:id>', views.book_shop_delate),
    path('genre/', views.genre_list),
    path('genre/add', views.genre_add),
    path('genre/show/<str:genre>', views.genre_detail),
    path('sale/', views.shop_sale),
    path('author/', views.author_list),
    path('author/show/<int:id>/', views.author_detail),
    path('author/add/', views.author_create),
    path('author/edite/<int:id>', views.author_update),
    path('author/del/', views.author_remove),
    path('book/', views.book_list, name = 'book_list'),
    path('book/add/', views.book_create),
    path('book/show/<int:id>/', views.book_detail),
    path('book/edite/<int:id>/', views.book_update),
    path('book/del/', views.book_remove),

    # Add only links for add parts
]
