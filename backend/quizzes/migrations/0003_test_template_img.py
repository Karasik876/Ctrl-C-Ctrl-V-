# Generated by Django 4.2.7 on 2023-12-26 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='template_img',
            field=models.TextField(default='', verbose_name='Шаблон'),
        ),
    ]
