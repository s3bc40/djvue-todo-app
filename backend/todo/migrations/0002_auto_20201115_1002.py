# Generated by Django 3.1.3 on 2020-11-15 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='tasks',
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(null=True, to='todo.Tag'),
        ),
    ]
