# Generated by Django 5.0.4 on 2024-04-17 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instav2', '0003_posts_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='users',
        ),
    ]
