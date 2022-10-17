from django.db import models


class Genre(models.TextChoices):
    historical_story = 'історична повість'
    novel = 'роман'
    fantasy = 'фантастика'
    comics = 'комікси'
    tales = 'казки'
    poems = 'вірші'
    prose = 'проза'

    def __str__(self):
        return self.name


class Currency(models.TextChoices):
    UAH = 'UAH'

    def __str__(self):
        return self.capitalize()


class Language(models.TextChoices):
    ukrainian = 'українська'
    english = 'англійська'

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)
class Book(models.Model):
    book_name = models.CharField(max_length=80)
    isbn = models.CharField('ISBN', max_length=13,
                            unique=True,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')
    year_of_issue = models.DateTimeField()
    book_language = models.CharField(choices=Language.choices, default=Language.ukrainian,max_length=20)
    genre = models.CharField(choices=Genre.choices, max_length=20)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    pic = models.ImageField(upload_to='static/img', blank=True)

    def __str__(self):
        return '{0}, {1}, {2}, {3}, {4}, {5}'.format(self.book_name.title(), self.year_of_issue, self.isbn,self.book_language,self.genre,self.author)

class Book_shop(models.Model):
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.01)
    currency = models.CharField(default=Currency.UAH, max_length=20)
    quantity = models.IntegerField()
    booked = models.IntegerField()
    sale = models.BooleanField(default=False)
    url = models.URLField(max_length=200,default='empty')


    def __str__(self):
        return '{0}, {1}, {2}, {3}, {4}, {5}'.format(self.book, self.price, self.currency,self.quantity,self.book,self.sale)

