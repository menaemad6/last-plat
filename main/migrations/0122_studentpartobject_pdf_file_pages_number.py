# Generated by Django 4.1.7 on 2024-08-25 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0121_part_pdf_file_pages_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentpartobject',
            name='pdf_file_pages_number',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
