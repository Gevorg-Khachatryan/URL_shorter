from django.db import models

class short_urls(models.Model):
    short_url = models.CharField(max_length=20,)
    long_url = models.URLField("Enter URL", unique=True)
    hits = models.IntegerField(default=0)
    user_index = models.IntegerField(default=0)



