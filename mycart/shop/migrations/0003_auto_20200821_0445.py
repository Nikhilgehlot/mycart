# Generated by Django 3.0.8 on 2020-08-21 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200817_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='', max_length=50),
        ),
    ]
