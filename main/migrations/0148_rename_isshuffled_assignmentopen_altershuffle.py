# Generated by Django 4.1.7 on 2025-01-02 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0147_assignment_shufflequestions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignmentopen',
            old_name='isShuffled',
            new_name='alterShuffle',
        ),
    ]