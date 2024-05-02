# Generated by Django 5.0.4 on 2024-04-17 12:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instav2', '0002_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
