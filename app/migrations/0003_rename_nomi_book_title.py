# Generated by Django 5.1 on 2025-03-05 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_title_book_nomi_alter_book_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='nomi',
            new_name='title',
        ),
    ]
