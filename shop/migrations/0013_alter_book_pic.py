# Generated by Django 4.1 on 2022-10-15 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_book_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pic',
            field=models.ImageField(blank=True, upload_to='static/img'),
        ),
    ]