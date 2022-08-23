from django.contrib import admin

from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    fields = ["title", "pub_date", "blog_text", "author"]
    search_fields = ["title"]


admin.site.register(Blog, BlogAdmin)