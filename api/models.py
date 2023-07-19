from django.db import models


# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')


class Subtitle(models.Model):
    video = models.ForeignKey(Video, related_name='subtitles', on_delete=models.CASCADE)
    text = models.TextField()
    time = models.FloatField()
