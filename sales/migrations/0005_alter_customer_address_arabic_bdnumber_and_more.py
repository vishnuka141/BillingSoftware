# Generated by Django 4.1 on 2022-08-30 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_alter_customer_address_arabic_bdnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_address',
            name='arabic_bdnumber',
            field=models.CharField(blank=True, default=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='customer_address',
            name='arabic_street',
            field=models.CharField(blank=True, default=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='customer_address',
            name='city_arabic',
            field=models.CharField(blank=True, default=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='customer_address',
            name='country_arabic',
            field=models.CharField(blank=True, default=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='customer_address',
            name='zipcode_arabic',
            field=models.CharField(blank=True, default=True, max_length=120),
        ),
    ]