# Generated by Django 4.1.7 on 2023-07-08 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='shoe_name',
            field=models.CharField(max_length=50),
        ),
    ]
