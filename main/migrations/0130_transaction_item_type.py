# Generated by Django 4.1.7 on 2024-09-05 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0129_alter_chaptermember_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='item_type',
            field=models.CharField(blank=True, choices=[('lecture', 'Lecture'), ('chapter', 'Chapter')], max_length=25, null=True),
        ),
    ]
