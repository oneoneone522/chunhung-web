# Generated by Django 5.0.7 on 2024-08-04 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_remove_quotationinfo_user_quotationinfo_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotationinfo',
            name='tax_code',
        ),
        migrations.AddField(
            model_name='quotationinfo',
            name='phonenum',
            field=models.CharField(default='07-7874443', max_length=20),
        ),
    ]
