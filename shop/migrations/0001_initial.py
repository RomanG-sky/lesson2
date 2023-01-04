# Generated by Django 4.1 on 2022-12-28 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('pic', models.ImageField(blank=True, upload_to='static/img')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=20)),
                ('isbn', models.CharField(help_text='Unique 13 character', max_length=13, unique=True, verbose_name='ISBN')),
                ('year_of_issue', models.DateTimeField()),
                ('book_language', models.CharField(choices=[('українська', 'Ukrainian'), ('англійська', 'English')], default='українська', max_length=20)),
                ('genre', models.CharField(choices=[('historical', 'Historical'), ('novel', 'Novel'), ('fantasy', 'Fantasy'), ('comics', 'Comics'), ('tales', 'Tales'), ('poems', 'Poems'), ('prose', 'Prose')], max_length=20)),
                ('pic', models.ImageField(blank=True, upload_to='static/img')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='shop.author')),
            ],
        ),
        migrations.CreateModel(
            name='Book_shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.01, max_digits=10)),
                ('currency', models.CharField(default='UAH', max_length=20)),
                ('quantity', models.IntegerField()),
                ('booked', models.IntegerField()),
                ('sale', models.BooleanField(default=False)),
                ('url', models.URLField(default='empty')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='shop.book')),
            ],
        ),
    ]
