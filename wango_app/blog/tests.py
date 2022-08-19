import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Blog


# Functions

def create_blogpost(title:str, blog_text:str, days:int) -> Blog:
    blogpost = Blog(title=title, blog_text=blog_text, pub_date= timezone.now() + datetime.timedelta(days=days))
    return blogpost


# Models test

## Blog model tests: 2
class BlogModelTest(TestCase):
    
    def test_was_published_recently_with_future_blogpost(self):
        """ The method was_published_recently of Blog model 
            returns False for future dates"""
        blogpost_1 = create_blogpost(
            title="Titulo de prueba",
            blog_text="Este es un blogpost de prueba",
            days=10
        )
        blogpost_2 = create_blogpost(
            title="Titulo de prueba 2",
            blog_text="Este es un segundo blogpost de prueba",
            days=1
        )
        self.assertIs(blogpost_1.was_published_recently(), False)
        self.assertIs(blogpost_2.was_published_recently(), False)

    def test_was_published_recently_with_past_question(self):
        """ The method was_published_recently of Blog model 
            returns True for past dates"""
        blogpost_1 = create_blogpost(
            title="Blogpost de hoy",
            blog_text="Este es un blogpost de prueba del día de hoy",
            days=0
        )
        blogpost_2 = create_blogpost(
            title="Blogpost de hace 1 dia",
            blog_text="Este es un segundo blogpost de prueba de hace un día",
            days=-1
        )
        blogpost_3 = create_blogpost(
            title="Blogpost de hace 2 dias",
            blog_text="Este es un segundo blogpost de prueba de hace un día",
            days=-2
        )
        blogpost_4 = create_blogpost(
            title="Blogpost de hace 10 dias",
            blog_text="Este es un segundo blogpost de prueba de hace 10 días",
            days=-10
        )
        self.assertIs(blogpost_1.was_published_recently(), True)
        self.assertIs(blogpost_2.was_published_recently(), True)
        self.assertIs(blogpost_3.was_published_recently(), False)
        self.assertIs(blogpost_4.was_published_recently(), False)


# Views test

## Index view tests: 
class IndexViewTest(TestCase):
    pass