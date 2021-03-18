# Generated by Django 3.1.7 on 2021-03-18 08:57

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_id', models.TextField()),
                ('title', models.CharField(max_length=200, verbose_name='Song name')),
                ('thumbnail', models.ImageField(upload_to='thumbnails')),
                ('song', models.FileField(upload_to=core.models.song_directory_path)),
                ('playtime', models.CharField(default='0.00', max_length=10)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('artists', models.ManyToManyField(related_name='songs', to='core.Artist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
