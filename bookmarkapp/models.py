from django.db import models
from taggit.managers import TaggableManager

class Bookmarks(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=150)
    desc = models.TextField()
    tags = TaggableManager()