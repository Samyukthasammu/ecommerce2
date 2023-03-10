# Generated by Django 3.2.16 on 2023-01-02 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seller', '0002_alter_product_stock'),
        ('common', '0005_rename_username_seller_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.product')),
            ],
        ),
    ]
