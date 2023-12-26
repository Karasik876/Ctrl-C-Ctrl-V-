# Generated by Django 4.2.7 on 2023-12-15 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_image', models.CharField(max_length=255, null=True, verbose_name='Имя')),
                ('sheet_image', models.CharField(max_length=255, null=True, verbose_name='Бланк')),
                ('student_answers', models.CharField(max_length=255, verbose_name='Ответы')),
                ('result', models.IntegerField(verbose_name='Кол-во баллов')),
                ('scanned_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата сканирования')),
                ('test', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quizzes.test', verbose_name='Тест')),
                ('the_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.class', verbose_name='Класс')),
            ],
        ),
    ]
