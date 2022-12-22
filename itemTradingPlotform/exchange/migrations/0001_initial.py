# Generated by Django 3.2 on 2022-10-07 10:16

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=11, null=True, unique=True, verbose_name='手机号')),
                ('avater', models.ImageField(null=True, upload_to='img/', verbose_name='头像')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emergency_degree', models.IntegerField(choices=[(1, 'Urgency'), (2, 'Norm'), (3, 'Looseness')], default=3, verbose_name='紧急程度')),
                ('material_type', models.CharField(choices=[('m', '医疗物资'), ('f', '食物'), ('d', '生活必须品')], default='d', max_length=8, verbose_name='物品种类')),
                ('body', models.CharField(max_length=100, verbose_name='需求信息')),
                ('pub_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布时间')),
                ('keywords', models.CharField(max_length=50, verbose_name='关键字')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.user')),
            ],
        ),
        migrations.CreateModel(
            name='Receive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='领取时间')),
                ('finish_time', models.DateTimeField(default=0, verbose_name='完成时间')),
                ('requirement_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.requirement')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.user')),
            ],
        ),
    ]
