# Generated by Django 3.2.7 on 2021-09-27 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_notebook_smartphone'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='for_anonymous_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='in_order',
            field=models.BooleanField(default=False),
        ),
    ]
