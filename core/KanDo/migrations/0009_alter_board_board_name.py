# Generated by Django 5.0.1 on 2024-01-05 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KanDo', '0008_alter_board_owner_alter_column_board_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='board_name',
            field=models.CharField(max_length=180),
        ),
    ]
