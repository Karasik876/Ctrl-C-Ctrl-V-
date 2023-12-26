# Generated by Django 4.2.7 on 2023-12-15 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(default='Новый класс', max_length=20, verbose_name='Название')),
                ('class_number', models.IntegerField(verbose_name='Класс')),
                ('class_letter', models.CharField(default='', max_length=1, verbose_name='Буква')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
            ],
        ),
    ]
