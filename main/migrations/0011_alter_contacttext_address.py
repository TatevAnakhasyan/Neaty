# Generated by Django 5.0.1 on 2024-01-19 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_contacttext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacttext',
            name='address',
            field=models.CharField(max_length=200, verbose_name='Address'),
        ),
    ]