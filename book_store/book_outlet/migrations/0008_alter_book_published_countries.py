# Generated by Django 5.0.6 on 2024-07-08 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0007_country_alter_address_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_countries',
            field=models.ManyToManyField(to='book_outlet.country'),
        ),
    ]
