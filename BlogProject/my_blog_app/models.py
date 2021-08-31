from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=200)
    sub_title=models.TextField(blank=True,null=True)
    banner=models.ImageField(blank=True,null=True)
    blog=models.TextField()
    posted_at=models.DateTimeField(auto_now=True)