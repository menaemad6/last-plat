# Generated by Django 4.1.7 on 2023-10-18 16:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0031_alter_buylesson_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='LectureCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_id', models.CharField(blank=True, max_length=8, null=True)),
                ('lecture_id', models.CharField(blank=True, max_length=100)),
                ('teacher', models.CharField(blank=True, max_length=100)),
                ('total_students', models.IntegerField(default=0)),
                ('used_times', models.IntegerField(default=0)),
                ('valid', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Lecture Code',
                'verbose_name_plural': 'Lecture Codes',
            },
        ),
    ]
