# Generated by Django 3.2.16 on 2022-12-17 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20221216_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='username',
            new_name='user_name',
        ),
    ]