# Generated by Django 4.1 on 2022-09-16 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_book_author_alter_book_book_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_shop',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='shop.book'),
        ),
    ]