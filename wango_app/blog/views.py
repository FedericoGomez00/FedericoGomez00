from django.utils import timezone
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Blog

def index(request):
    return render(request, "blog/index.html", {})

class HomeView(LoginRequiredMixin ,generic.ListView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    template_name: str = "blog/home.html"
    context_object_name: str = "latest_blog_list"

    def get_queryset(self):
        return Blog.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")


class LoanedBlogpostByUserView(LoginRequiredMixin, generic.ListView):
    model = Blog
    template_name: str = "blog/my-blogposts.html"
    context_object_name: str = "my_blogposts"

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)


@login_required
def publish_blogpost(request):
    return render(request, "blog/publish.html", {})


def published_blogpost(request):
    try:
        title = request.POST["title_text"]
        body = request.POST["body_text"]
        user = request.user
    except (KeyError):
        print("La llave no existe")
    else:
        blogpost = Blog(title=title, blog_text=body, author=user).save()
        return HttpResponseRedirect(reverse("blog:home"))


class SearchView(generic.DetailView):
    model = Blog
    template_name: str = "blog/results.html"