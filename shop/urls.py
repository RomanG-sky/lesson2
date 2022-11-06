from django.urls import path
from shop import views

urlpatterns = [
    path('', views.base),
    path('add/',views.book_shop_add),
    path('edite/',views.book_shop_edite),
    path('comics/',views.shop_comics),
    path('historical/',views.shop_historical),
    path('poems/',views.shop_poems),
    path('genre/', views.genre),
    path('genre/add', views.genre_add),
    path('show/<int:id>/', views.book_shop_show),
    path('sale/', views.shop_sale),
    path('books/',views.books),
    path('author/',views.author),
    # path('author/<str:last_name><str:first_name>/', views.author_show),
    path('author/add/', views.author_add),
    # path('author/edite/', views.author_update),
    # path('author/del/', views.author_remove),
    path('books/add/', views.book_add),
    # path('book/show/', views.book_show),
    # path('book/edite/', views.book_update),
    # path('book/del/', views.book_remove),
    # path('book_shop/add', views.book_shop_add_sell),

    # path('book_shop/edite', views.book_shop_update_sell),
    # path('book_shop/del', views.book_shop_remove_sell)
    # Add only links for add parts
]