from my_blog_app.models import Blog
from django.shortcuts import redirect, render
from django.http import HttpResponse


def home(request):
    return render(request,'index.html')

def about_us(request):
    return render(request,'about_us.html')

def single_post(request,pk):
    return render(request,'post.html')

def contact(request):
    return render(request,'contact.html')

def write_post(request):
    if request.method=='POST':
        title=request.POST['title']
        subtitle=request.POST['subtitle']
        bannerImg=request.POST['bannerImg']
        blog=request.POST['blog']
        newBlog=Blog.objects.create(title=title,sub_title=subtitle,banner=bannerImg,blog=blog)
        newBlog.save()
        return redirect(request.META['HTTP_REFERER'])
    return render(request,'write_post.html')