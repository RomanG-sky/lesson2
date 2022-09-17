# Generated by Django 4.1 on 2022-09-15 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=80)),
                ('isbn', models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, unique=True, verbose_name='ISBN')),
                ('year_of_issue', models.DateTimeField()),
                ('book_language', models.CharField(choices=[('українська', 'Ukrainian'), ('англійська', 'English')], default='українська', max_length=20)),
                ('genre', models.CharField(choices=[('історична повість', 'Historical Story'), ('роман', 'Novel'), ('фантастика', 'Fantasy'), ('комікси', 'Comics'), ('казки', 'Tales')], max_length=20)),
                ('author', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='book_shop',
            name='book',
            field=models.CharField(max_length=100),
        ),
    ]
