# Generated by Django 3.1.1 on 2021-01-31 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheats_app', '0003_books_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='books_module',
            name='book_link',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]
