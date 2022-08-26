# Generated by Django 4.1 on 2022-08-25 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=250)),
                ('customer_displayname', models.CharField(max_length=120)),
                ('display_name_arabic', models.CharField(max_length=200, null=True)),
                ('cusotmer_email', models.EmailField(max_length=254)),
                ('customer_phone', models.CharField(max_length=120)),
                ('buyer_id_options', models.CharField(choices=[('NAT', 'NAT'), ('TIN', 'TIN'), ('IQA', 'IQA'), ('PAS', 'PAS'), ('CRN', 'CRN'), ('MOM', 'MOM'), ('MLS', 'MLS'), ('SAG', 'SAG'), ('GCC', 'GCC'), ('OTH', 'OTH')], default='NAT', max_length=120)),
                ('buyer_id', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_or_region', models.CharField(max_length=120)),
                ('country_arabic', models.CharField(max_length=120, null=True)),
                ('building_number', models.CharField(max_length=120)),
                ('arabic_bdnumber', models.CharField(max_length=120, null=True)),
                ('street', models.CharField(max_length=120)),
                ('arabic_street', models.CharField(max_length=120, null=True)),
                ('city', models.CharField(max_length=120)),
                ('city_arabic', models.CharField(max_length=250, null=True)),
                ('zipcode', models.CharField(max_length=120)),
                ('zipcode_arabic', models.CharField(max_length=120, null=True)),
                ('phone_no', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Quote_Items',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_details', models.CharField(max_length=120)),
                ('quantity', models.PositiveIntegerField()),
                ('rate', models.FloatField()),
                ('discount', models.FloatField()),
                ('tax', models.FloatField()),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('quote_id', models.AutoField(primary_key=True, serialize=False)),
                ('quote_date', models.DateField(auto_now_add=True)),
                ('quote_expdate', models.DateField()),
                ('quote_status', models.CharField(choices=[('pending', 'pending'), ('approved', 'approved'), ('cancelled', 'cancelled'), ('expired', 'expired')], default='pending', max_length=120)),
                ('customer_notes', models.TextField()),
                ('terms_and_conditions', models.TextField()),
                ('customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_name', to='sales.customer')),
                ('quote_createdby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quote_createdby', to='sales.customer')),
                ('quote_items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quote_items', to='sales.quote_items')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='adddress',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='sales.customer_address'),
        ),
        migrations.AddField(
            model_name='customer',
            name='created_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
