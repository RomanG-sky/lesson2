from django.db import models

# Create your models here.
class Post(models.Model):
    class Currency(models.TextChoices):
        UAH = "Hryvnya"
        USD = "US Dollar"
        EUR = "Euro"
    title = models.CharField(max_length=40)
    content = models.TextField()
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    # add price field with enum class for basic currency
    currency = models.CharField(max_length=10,choices= Currency.choices, default=Currency.UAH)
    # enum class for basic currency
    url_instruction = models.URLField(default='www.write_something.com')
    # add field for link of instruction or site of company
    make_response = models.BooleanField(default=True)
    # field for choose permits or not to make response
    response = models.TextField()
    # didn't know how to use condition/ if make_response is True: response...



    def __str__(self):
        return self.title