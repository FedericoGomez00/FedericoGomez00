from django.utils import timezone
from django.views import generic
from django.shortcuts import render

from .models import Blog

class IndexView(generic.ListView):
    template_name: str = "blog/index.html"
    context_object_name: str = "latest_blog_list"

    def get_queryset(self):
        return Blog.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")