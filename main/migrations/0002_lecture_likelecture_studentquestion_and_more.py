# Generated by Django 4.1.7 on 2023-10-07 21:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, max_length=100)),
                ('video', models.FileField(blank=True, upload_to='lessons')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('caption', models.TextField(blank=True)),
                ('image', models.ImageField(default='none.jpeg', upload_to='lecture_images')),
                ('price', models.IntegerField(default=0)),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('parts_number', models.IntegerField(default=0)),
                ('no_of_buys', models.IntegerField(default=0)),
                ('no_of_likes', models.IntegerField(default=0)),
                ('no_of_comments', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('teacher_name', models.CharField(blank=True, max_length=100, null=True)),
                ('teacher_img', models.ImageField(blank=True, null=True, upload_to='teacher_images')),
                ('year', models.CharField(blank=True, choices=[('first', 'First'), ('second', 'Second'), ('third', 'Third')], default='first', max_length=25)),
                ('type', models.CharField(blank=True, choices=[('normal', 'Normal'), ('chapter', 'Chapter'), ('group', 'Group')], default='normal', max_length=25)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Lecture',
                'verbose_name_plural': 'Lectures',
            },
        ),
        migrations.CreateModel(
            name='LikeLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=100)),
                ('user_image', models.ImageField(default='blank-profile-picture.png', upload_to='profile_images')),
                ('lecture_id', models.CharField(max_length=500)),
                ('liked_at', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
            },
        ),
        migrations.CreateModel(
            name='StudentQuestion',
            fields=[
                ('comment_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('lecture_id', models.CharField(blank=True, max_length=500)),
                ('user_name', models.CharField(blank=True, max_length=100)),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='profile_images')),
                ('commented_to', models.CharField(blank=True, max_length=100)),
                ('comment', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('no_of_likes', models.IntegerField(default=0)),
                ('no_of_answers', models.IntegerField(default=0)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Student Question',
                'verbose_name_plural': 'Student Questions',
            },
        ),
        migrations.CreateModel(
            name='StudentQuestionAnswer',
            fields=[
                ('answer_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('question_id', models.CharField(max_length=500)),
                ('user_name', models.CharField(blank=True, max_length=100)),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='profile_images')),
                ('answered_to', models.CharField(blank=True, max_length=100)),
                ('question_text', models.CharField(blank=True, max_length=500)),
                ('answer', models.CharField(blank=True, max_length=500)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('no_of_likes', models.IntegerField(default=0)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Student Question Answer',
                'verbose_name_plural': 'Student Question Answer',
            },
        ),
        migrations.DeleteModel(
            name='AssignmentResult',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='FollowersCount',
        ),
        migrations.DeleteModel(
            name='Instructor',
        ),
        migrations.DeleteModel(
            name='LikePost',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.AlterModelOptions(
            name='chapterlecture',
            options={'verbose_name': 'Chapter Lecture', 'verbose_name_plural': 'Chapter Lectures'},
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='number',
            new_name='question_number',
        ),
        migrations.RenameField(
            model_name='assignment',
            old_name='post_id',
            new_name='lecture_id',
        ),
        migrations.RenameField(
            model_name='assignmentsubmit',
            old_name='created_at',
            new_name='submited_at',
        ),
        migrations.RenameField(
            model_name='buychapter',
            old_name='image',
            new_name='user_image',
        ),
        migrations.RenameField(
            model_name='buychapter',
            old_name='name',
            new_name='user_name',
        ),
        migrations.RenameField(
            model_name='buylesson',
            old_name='post_id',
            new_name='lecture_id',
        ),
        migrations.RenameField(
            model_name='buylesson',
            old_name='image',
            new_name='user_image',
        ),
        migrations.RenameField(
            model_name='buylesson',
            old_name='name',
            new_name='user_name',
        ),
        migrations.RenameField(
            model_name='groupmember',
            old_name='member',
            new_name='member_name',
        ),
        migrations.RenameField(
            model_name='groupmember',
            old_name='name',
            new_name='user_name',
        ),
        migrations.RenameField(
            model_name='part',
            old_name='teacher',
            new_name='user_name',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='number',
            new_name='question_number',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='username',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='username',
        ),
        migrations.RemoveField(
            model_name='assignmentopen',
            name='username',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer1',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer10',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer11',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer12',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer13',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer14',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer15',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer16',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer17',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer18',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer19',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer2',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer20',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer21',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer22',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer23',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer24',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer25',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer26',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer27',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer28',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer29',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer3',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer30',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer31',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer32',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer33',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer34',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer35',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer36',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer37',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer38',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer39',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer4',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer40',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer41',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer42',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer43',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer44',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer45',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer46',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer47',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer48',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer49',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer5',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer50',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer6',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer7',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer8',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='answer9',
        ),
        migrations.RemoveField(
            model_name='assignmentsubmit',
            name='username',
        ),
        migrations.RemoveField(
            model_name='buychapter',
            name='username',
        ),
        migrations.RemoveField(
            model_name='buylesson',
            name='username',
        ),
        migrations.RemoveField(
            model_name='part',
            name='place',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='question',
            name='username',
        ),
        migrations.RemoveField(
            model_name='rechargerequest',
            name='username',
        ),
        migrations.AddField(
            model_name='answer',
            name='assignment_name',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='answer',
            name='question_image',
            field=models.ImageField(blank=True, default='blank-profile-picture.png', null=True, upload_to='questions'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='user_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='assignment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assignment',
            name='user_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='assignmentopen',
            name='start_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='assignmentopen',
            name='timer',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='assignmentopen',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assignmentopen',
            name='user_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='assignmentsubmit',
            name='opened_at',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='assignmentsubmit',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assignmentsubmit',
            name='user_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='buychapter',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='buylesson',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chapter',
            name='user_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='group',
            name='user_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='groupmember',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='news',
            name='user_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='part',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='question_image',
            field=models.ImageField(blank=True, default='blank-profile-picture.png', null=True, upload_to='questions'),
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(blank=True, choices=[('normal', 'Normal'), ('image_ar', 'Image Ar'), ('image_en', 'Image En')], default='normal', max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='user_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='rechargerequest',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rechargerequest',
            name='user_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chapterlecture',
            name='image',
            field=models.ImageField(default='none.jpeg', upload_to='lecture_images'),
        ),
        migrations.AlterField(
            model_name='group',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grouplecture',
            name='image',
            field=models.ImageField(default='none.jpeg', upload_to='lecture_images'),
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
