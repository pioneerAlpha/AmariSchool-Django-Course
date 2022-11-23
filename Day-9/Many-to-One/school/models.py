from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    post_title = models.CharField(max_length = 70)
    post_cat = models.CharField(max_length = 70)
    post_publish_date = models.DateField()