# Generated by Django 4.2.2 on 2023-07-18 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.URLField(max_length=300),
        ),
    ]
