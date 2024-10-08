# Generated by Django 5.0.7 on 2024-08-06 17:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_profile_profile_picture'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Completed', 'Completed')], default='Pending', max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='productreview',
            unique_together={('product', 'user')},
        ),
    ]
