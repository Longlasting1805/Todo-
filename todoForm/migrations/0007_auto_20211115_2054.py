# Generated by Django 3.2.3 on 2021-11-15 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoForm', '0006_auto_20210930_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='validation_model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='validation_model',
            name='save',
            field=models.BooleanField(default=False),
        ),
    ]
