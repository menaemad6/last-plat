# Generated by Django 4.1.7 on 2024-09-12 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0139_profile_true_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='custom_player_url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]