# Generated by Django 4.1.7 on 2025-01-05 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0150_assignment_qr_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='qr_code',
            field=models.ImageField(blank=True, default='blank-lecture.jpeg', null=True, upload_to='qr-codes'),
        ),
    ]
