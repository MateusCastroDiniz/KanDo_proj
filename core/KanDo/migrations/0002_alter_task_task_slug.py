# Generated by Django 5.0.1 on 2024-01-05 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KanDo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_slug',
            field=models.CharField(max_length=200, verbose_name='<django.db.models.fields.CharField>'),
        ),
    ]
