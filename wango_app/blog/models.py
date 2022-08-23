import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(
        max_length=20,
        help_text="Enter the title",
        verbose_name="Title"
        )
    blog_text = models.TextField(
        max_length=255,
        help_text="Enter the body of the blogpost",
        verbose_name="Body"
        )
    pub_date = models.DateField(
        help_text="Enter the publication date",
        verbose_name="Publication date",
        default=timezone.now()
        )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title

    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)