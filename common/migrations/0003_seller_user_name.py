# Generated by Django 3.2.16 on 2022-12-15 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='user_name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
