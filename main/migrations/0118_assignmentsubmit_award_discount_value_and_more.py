# Generated by Django 4.1.7 on 2024-08-25 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0117_lecturediscount_awarded_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentsubmit',
            name='award_discount_value',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='assignmentsubmit',
            name='award_lecture_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='assignmentsubmit',
            name='award_lecture_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]