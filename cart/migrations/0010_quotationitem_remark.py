# Generated by Django 5.0.7 on 2024-08-07 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_remove_quotationinfo_tax_code_quotationinfo_phonenum'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotationitem',
            name='remark',
            field=models.TextField(default='leave your remark'),
        ),
    ]
