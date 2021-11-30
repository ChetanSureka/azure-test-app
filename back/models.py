from django.db import models

class Categories(models.Model):
    id = models.AutoField(verbose_name='Category ID', primary_key=True, blank=False, auto_created=True)
    name = models.CharField(verbose_name='Category Name', blank=False, max_length=50)
    datecreated = models.DateTimeField(verbose_name='Date Created', auto_now=True)

    def __str__(self):
        return str(self.name)

class Playlists(models.Model):
    id = models.AutoField(verbose_name='ID', primary_key=True, unique=True, blank=False, auto_created=True)
    category = models.ForeignKey(verbose_name='Category', to=Categories, on_delete=models.CASCADE, related_name="playlist_category")
    url = models.URLField(verbose_name='Playlist URL', default="Enter the URL here", blank=False)
    channelname = models.CharField(verbose_name="Channel Name", max_length=100, blank=True)
    datecreated = models.DateTimeField(verbose_name='Date Created', auto_now=True)

    def __str__(self):
        return str(self.id)