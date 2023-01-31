from django.db import models

#
# class Genre(models.TextChoices):
#     historical = 'historical',
#     novel = 'novel',
#     fantasy = 'fantasy',
#     comics = 'comics',
#     tales = 'tales',
#     poems = 'poems',
#     prose = 'prose'
#
#     def __str__(self):
#         return self.name


class Currency(models.TextChoices):
    UAH = 'UAH'

    def __str__(self):
        return self


class Language(models.TextChoices):
    ukrainian = 'українська'
    english = 'англійська'

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    pic = models.ImageField(upload_to='static/img', blank=True)

    def author_id(self):
        return f'{self.id}'

    def get_absolut_url_author(self):
        return f'/shop/author/show/{self.id}'

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name, )


def Book_genre():
    genre = [
        ('historical', 'historical'),
        ('novel', 'novel'),
        ('fantasy', 'fantasy'),
        ('comics', 'comics'),
        ('tales', 'tales'),
        ('poems', 'poems'),
        ('prose', 'prose')
    ]
    return genre


class Book(models.Model):
    genre_ls = [
        ('historical', 'historical'),
        ('novel', 'novel'),
        ('fantasy', 'fantasy'),
        ('comics', 'comics'),
        ('tales', 'tales'),
        ('poems', 'poems'),
        ('prose', 'prose')
    ]
    book_name = models.CharField(max_length=20)
    isbn = models.CharField('ISBN', max_length=13,
                            unique=True,
                            help_text='Unique 13 character')
    year_of_issue = models.DateTimeField()
    book_language = models.CharField(choices=Language.choices, default=Language.ukrainian, max_length=20)
    genre = models.CharField(choices=Book_genre(), max_length=20, default='prose')
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    pic = models.ImageField(upload_to='static/img', blank=True)

    def genre_id(self):
        return f'/shop/genre/show/{self.id}'
    def book_id(self):
        return f'{self.id}'

    def get_absolut_url_book(self):
        return f'/shop/book/show/{self.id}'

    def __str__(self):
        return '{0}, {1}, {2}, {3}, {4}, {5}'.format(self.book_name.title(), self.year_of_issue, self.isbn,
                                                     self.book_language, self.genre, self.author)


class Book_shop(models.Model):
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.01)
    currency = models.CharField(default=Currency.UAH, max_length=20)
    quantity = models.IntegerField()
    booked = models.IntegerField()
    sale = models.BooleanField(default=False)
    url = models.URLField(max_length=200, default='empty')

    def genre_id(self):
        return f'/shop/genre/show/{self.id}'

    def get_absolut_url(self):
        return f'/shop/show/{self.id}'

    def __str__(self):
        return '{0}, {1}, {2}, {3}, {4}, {5}'.format(self.book, self.price, self.currency, self.quantity, self.book,
                                                     self.sale)
