from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("my-blogposts/", views.LoanedBlogpostByUserView.as_view(), name="my_blogposts"),
    path("publish/", views.publish_blogpost, name="publish_blogpost"),
    path("published/", views.published_blogpost, name="published_blogpost")
]
