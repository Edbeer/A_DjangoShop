# Generated by Django 3.2.7 on 2021-09-28 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20210928_2212'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CategoryManager',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
    ]
