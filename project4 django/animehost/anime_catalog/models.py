from django.db import models

class Anime(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    video_url = models.URLField(max_length=200, default='https://www.youtube.com/watch?v=RHv5r36fX7k')

    def __str__(self):
        return self.title
