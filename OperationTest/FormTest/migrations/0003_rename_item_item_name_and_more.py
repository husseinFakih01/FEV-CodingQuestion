# Generated by Django 4.0.5 on 2022-06-11 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FormTest', '0002_rename_datepurchased_item_dateadded'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='enjoyedItem',
            new_name='purchased',
        ),
    ]
