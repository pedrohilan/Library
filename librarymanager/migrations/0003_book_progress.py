# Generated by Django 4.1.2 on 2022-12-13 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarymanager', '0002_book_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='progress',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
