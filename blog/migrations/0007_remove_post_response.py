# Generated by Django 4.1 on 2022-09-09 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_instruction_post_url_instruction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='response',
        ),
    ]
