# Generated by Django 5.0.7 on 2024-08-05 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0008_alter_todolist_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='tasks',
            field=models.ManyToManyField(blank=True, to='todo_list.task'),
        ),
    ]
