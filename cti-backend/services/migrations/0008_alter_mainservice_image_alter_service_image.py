# Generated by Django 5.0.3 on 2024-03-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_mainservice_description_alter_service_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainservice',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
