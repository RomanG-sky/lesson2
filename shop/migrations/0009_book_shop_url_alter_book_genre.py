# Generated by Django 4.1 on 2022-10-14 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_remove_book_author_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_shop',
            name='url',
            field=models.URLField(default='empty'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('історична повість', 'Historical Story'), ('роман', 'Novel'), ('фантастика', 'Fantasy'), ('комікси', 'Comics'), ('казки', 'Tales'), ('вірші', 'Poems'), ('проза', 'Prose')], max_length=20),
        ),
    ]
