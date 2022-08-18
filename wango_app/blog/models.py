import datetime

from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=20)
    blog_text = models.CharField(max_length=255)
    pub_date = models.DateField("date published")

    def __str__(self) -> str:
        return self.title

    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)