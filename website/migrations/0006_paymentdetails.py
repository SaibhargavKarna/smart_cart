# Generated by Django 4.2.2 on 2023-11-17 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_order_shippingaddress_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='paymentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=20)),
                ('order_id', models.CharField(blank=True, max_length=100)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]
