# Generated by Django 4.1.5 on 2023-05-07 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_podaci_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='podaci',
            name='price_kg',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
