# Generated by Django 5.0.7 on 2024-08-13 12:37

import datetime
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0010_alter_task_deadline_alter_task_description_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(default=datetime.datetime.now, verbose_name='تاریخ سررسید'),
        ),
        migrations.AlterField(
            model_name='tasklink',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_list.task', verbose_name='نام وظیفه'),
        ),
        migrations.AlterField(
            model_name='tasklink',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='لینک کوتاه شده'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='name',
            field=models.CharField(max_length=100, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='tasks',
            field=models.ManyToManyField(blank=True, to='todo_list.task', verbose_name='وظیفه ها'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
