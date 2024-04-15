# Generated by Django 5.0.3 on 2024-03-25 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_mainservice_field_name_service_field_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainservice',
            name='field_name',
        ),
        migrations.RemoveField(
            model_name='service',
            name='field_name',
        ),
        migrations.AddField(
            model_name='mainservice',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]