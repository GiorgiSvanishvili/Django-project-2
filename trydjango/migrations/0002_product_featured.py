# Generated by Django 2.1.5 on 2020-12-14 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trydjango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True),
        ),
    ]