# Generated by Django 4.1.7 on 2024-08-30 19:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0124_chapter_qr_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChapterMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=100)),
                ('member_name', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(default='blank-profile-picture.png', upload_to='profile_images')),
                ('chapter_id', models.CharField(blank=True, max_length=100)),
                ('chapter_title', models.CharField(blank=True, max_length=100)),
                ('method', models.CharField(blank=True, choices=[('admin', 'Admin'), ('code', 'Code'), ('qr_code', 'Qr Code'), ('link', 'Link'), ('request', 'Request')], default='admin', max_length=25)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Chapter Member',
                'verbose_name_plural': 'Chapter Members',
            },
        ),
    ]
