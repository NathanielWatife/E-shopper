# Generated by Django 5.0.7 on 2024-08-08 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='', null=True, upload_to='profile_pics/'),
        ),
    ]
