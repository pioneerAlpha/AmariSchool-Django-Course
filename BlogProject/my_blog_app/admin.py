from django.contrib import admin
from my_blog_app.models import Blog 

class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = ("js/tinymce.js",)
    list_display=['title','posted_at',]

admin.site.register(Blog,BlogAdmin)