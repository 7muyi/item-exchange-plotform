# Generated by Django 3.2 on 2022-10-08 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0002_auto_20221007_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='a', max_length=50, verbose_name='地址'),
        ),
        migrations.AddField(
            model_name='user',
            name='houser_numbser',
            field=models.CharField(default='a', max_length=30, verbose_name='门牌号'),
        ),
    ]
