# Generated by Django 3.2.7 on 2021-09-28 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210928_2206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notebook',
            old_name='categories',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='smartphone',
            old_name='categories',
            new_name='category',
        ),
    ]