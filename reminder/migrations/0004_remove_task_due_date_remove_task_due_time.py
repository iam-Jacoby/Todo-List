# Generated by Django 4.1.7 on 2023-12-29 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0003_task_due_date_task_due_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='due_time',
        ),
    ]
