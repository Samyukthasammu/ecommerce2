# Generated by Django 3.2.16 on 2022-12-16 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_seller_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='user_name',
            new_name='password',
        ),
        migrations.AddField(
            model_name='seller',
            name='username',
            field=models.CharField(default='', max_length=20),
        ),
    ]
