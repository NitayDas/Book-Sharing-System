# Generated by Django 4.2.6 on 2024-01-10 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0004_remove_bookrequest_is_approved_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='availability',
            field=models.IntegerField(default=9),
        ),
    ]