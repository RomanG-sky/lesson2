# Generated by Django 4.1 on 2022-09-16 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_book_alter_book_shop_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_name',
            field=models.CharField(choices=[('Кобзар', 'Kobzar')], max_length=80),
        ),
        migrations.AlterField(
            model_name='book_shop',
            name='book',
            field=models.CharField(choices=[('Кобзар', 'Kobzar')], max_length=50),
        ),
    ]
