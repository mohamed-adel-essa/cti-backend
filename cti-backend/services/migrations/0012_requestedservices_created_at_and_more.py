# Generated by Django 5.0.3 on 2024-04-16 12:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_alter_category_image_alter_service_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestedservices',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requestedservices',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
