# Generated by Django 4.2 on 2023-04-22 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_owner_book_ownertest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='ownertest',
            new_name='owner',
        ),
    ]
