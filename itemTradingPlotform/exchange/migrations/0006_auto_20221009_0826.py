# Generated by Django 3.2 on 2022-10-09 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0005_rename_user_id_requirement_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.RemoveField(
            model_name='requirement',
            name='user',
        ),
        migrations.AddField(
            model_name='requirement',
            name='finish_time',
            field=models.DateField(blank=True, null=True, verbose_name='完成时间'),
        ),
        migrations.AddField(
            model_name='requirement',
            name='pub_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='pub_user', to=settings.AUTH_USER_MODEL, verbose_name='发布用户'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requirement',
            name='rec_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='接收时间'),
        ),
        migrations.AddField(
            model_name='requirement',
            name='rec_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rec_user', to='exchange.user', verbose_name='接收用户'),
        ),
        migrations.AddField(
            model_name='requirement',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Unreceived'), (2, 'Received'), (3, 'Finish')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='material_type',
            field=models.CharField(choices=[('m', '医疗物资'), ('f', '食物'), ('d', '生活必须品'), ('o', '其他')], default='d', max_length=8, verbose_name='物品种类'),
        ),
        migrations.DeleteModel(
            name='Receive',
        ),
    ]
