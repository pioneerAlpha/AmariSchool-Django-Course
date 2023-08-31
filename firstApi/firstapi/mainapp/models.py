from django.db import models

# Create your models here.
# class List(models.Model):
#     name=models.CharField(max_length=100, blank=True, default='')
#     description=models.TextField()
    
#     def __str__(self):
#         return self.name
    
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return '%d: %s' % (self.order, self.title)