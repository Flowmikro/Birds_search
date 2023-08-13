# Generated by Django 4.2.4 on 2023-08-13 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BirdModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True, verbose_name='Название')),
                ('image', models.ImageField(blank=True, upload_to='media/', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='AddBirdModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('city', models.CharField(default=None, max_length=60, verbose_name='Город')),
                ('region', models.CharField(default=None, max_length=60, verbose_name='Район')),
                ('street', models.CharField(default=None, max_length=60, verbose_name='Улица')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('bird', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='birds.birdmodel', verbose_name='Птица')),
            ],
        ),
    ]