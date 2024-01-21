# Generated by Django 5.0.1 on 2024-01-16 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_galleryone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryone',
            name='image',
        ),
        migrations.AddField(
            model_name='galleryone',
            name='image1',
            field=models.ImageField(null=True, upload_to='media', verbose_name='First Image'),
        ),
        migrations.AddField(
            model_name='galleryone',
            name='image2',
            field=models.ImageField(null=True, upload_to='media', verbose_name='Second Image'),
        ),
        migrations.AddField(
            model_name='galleryone',
            name='image3',
            field=models.ImageField(null=True, upload_to='media', verbose_name='Third Image'),
        ),
        migrations.AddField(
            model_name='galleryone',
            name='image4',
            field=models.ImageField(null=True, upload_to='media', verbose_name='Fourth Image'),
        ),
        migrations.AddField(
            model_name='galleryone',
            name='image5',
            field=models.ImageField(null=True, upload_to='media', verbose_name='Fifth Image'),
        ),
    ]
