# Generated by Django 4.1.7 on 2024-09-05 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0131_alter_transaction_item_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buychapter',
            name='method',
            field=models.CharField(blank=True, choices=[('wallet', 'Wallet'), ('chapter_code', 'Chapter Code'), ('admin', 'Admin'), ('link', 'Link'), ('qr_code', 'Qr Code')], default='wallet', max_length=25),
        ),
    ]