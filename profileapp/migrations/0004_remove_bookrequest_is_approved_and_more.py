# Generated by Django 4.2.6 on 2024-01-10 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0003_alter_bookrequest_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookrequest',
            name='is_approved',
        ),
        migrations.AlterField(
            model_name='book',
            name='availability',
            field=models.IntegerField(default=0),
        ),
    ]