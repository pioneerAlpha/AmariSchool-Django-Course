from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=200)
    sub_title=models.TextField(blank=True,null=True)
    banner=models.ImageField(upload_to='banners',max_length=250,blank=True,null=True)
    blog=models.TextField()
    author=models.CharField(max_length=200,blank=True,null=True)
    author_email=models.EmailField(blank=True,null=True)
    posted_at=models.DateTimeField(auto_now=True)