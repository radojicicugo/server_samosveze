# Generated by Django 4.1.5 on 2023-05-02 07:11

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Podaci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/images')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('description', models.CharField(max_length=500)),
                ('klass', models.CharField(max_length=50)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
    ]
