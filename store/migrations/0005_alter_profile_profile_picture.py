# Generated by Django 5.0.7 on 2024-08-08 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_category_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='profile_pics/'),
        ),
    ]