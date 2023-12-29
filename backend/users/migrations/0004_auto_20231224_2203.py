# Generated by Django 3.2.23 on 2023-12-24 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_useraccount_email_alter_useraccount_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='first_name',
            field=models.CharField(max_length=12, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Прошел активацию'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Служебный аккаунт'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='last_name',
            field=models.CharField(max_length=12, verbose_name='Фамилия'),
        ),
    ]
