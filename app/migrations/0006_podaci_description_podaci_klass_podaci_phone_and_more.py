# Generated by Django 4.1.5 on 2023-05-04 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_podaci_image_alter_podaci_email_alter_podaci_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='podaci',
            name='description',
            field=models.EmailField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='podaci',
            name='klass',
            field=models.EmailField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='podaci',
            name='phone',
            field=models.EmailField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='podaci',
            name='price',
            field=models.EmailField(max_length=10, null=True),
        ),
    ]