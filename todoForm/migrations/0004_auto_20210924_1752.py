# Generated by Django 2.2.5 on 2021-09-24 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoForm', '0003_auto_20210924_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_loginmodel',
            name='username',
            field=models.EmailField(max_length=100),
        ),
    ]