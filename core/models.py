import math
from time import strftime, gmtime

from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
import datetime

from accounts.models import User


def song_directory_path(instance, filename):
    return 'songs/{0}/{1}'.format(strftime('%Y/%m/%d'), generate_file_name() + '.' + filename.split('.')[-1])

def generate_file_name(length=30):
    letters = string.ascii_letters + string.digits
    return ''.join(choice(letters) for _ in range(length))


class Artist(models.Model):
    name=models.CharField(max_length=100)


class Song(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_id = models.TextField()
    title = models.TextField(max_length=200, verbose_name="Song name")
    thumbnail = models.ImageField(upload_to="thumbnails", blank=False)
    song = models.FileField(upload_to=song_directory_path)
    artists = models.ManyToManyField(Artist,related_name='songs')
    playtime = models.CharField(max_length=10, default="0.00")

    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)


    def __str__(self):
        return self.title

    @property
    def duration(self):
        return str(strftime('%H:%M:%S', gmtime(float(self.playtime))))

