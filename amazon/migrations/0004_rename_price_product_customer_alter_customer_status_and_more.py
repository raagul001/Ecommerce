# Generated by Django 5.1 on 2024-08-26 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0003_customer_alter_product_status_alter_product_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='customer',
        ),
        migrations.AlterField(
            model_name='customer',
            name='Status',
            field=models.BooleanField(default=False, help_text='0-show, 1-hidden'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Status',
            field=models.BooleanField(default=False, help_text='0-show, 1-hidden'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Trending',
            field=models.BooleanField(default=False, help_text='0-default, 1-trending'),
        ),
    ]
