from my_blog_app.models import Blog
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
# cleanup_old_files
from django.apps import apps
apps.get_models()

def home(request):
    data=Blog.objects.all()
    return render(request,'index.html',{'blogs':data})

def about_us(request):
    return render(request,'about_us.html')

def user_profile(request):
    return render(request,'user_profile.html')

def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,'Login Successful')
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials')
            return render(request,'login.html')
        
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            try:
                user=User.objects.create_user(username=email,email=email,first_name=name,password=password)
                user.save()
                messages.success(request,'Sign Up Successful.')
                return redirect('login')
            except Exception as e:
                messages.error(request,"Email already exists.")
                return redirect(request.META['HTTP_REFERER'])
        else:
            messages.warning(request,'Confirm password is not matching.')
            return redirect(request.META['HTTP_REFERER'])

    return render(request,'signup.html')

def my_blogs(request):
    author_email=request.user.email
    my_blogs=Blog.objects.all().filter(author_email=author_email)
    return render(request,'my_blogs.html',{'blogs':my_blogs})

def single_post(request,pk):
    singleBlog=Blog.objects.get(pk=pk)
    return render(request,'post.html',{'singleBlog':singleBlog})

def contact(request):
    return render(request,'contact.html')

def update_post(request,id):
    try:
        single_blog=Blog.objects.get(pk=id)
        if request.user.email==single_blog.author_email:
            if request.method=="POST":
                title=request.POST['title']
                subtitle=request.POST['subtitle'] 
             
                blog=request.POST['blog']
                if title !="":
                    single_blog.title=title
                if subtitle!="":
                    single_blog.sub_title=subtitle
                if blog!="":
                    single_blog.blog=blog
                try:
                    banner=request.FILES['banner_image']
                    single_blog.banner=banner
                except:
                    single_blog.banner=single_blog.banner
                    
                single_blog.save()
                messages.success(request,'Blog is updated successfully.')
                return redirect('my_blogs')
            return render(request,'update_post.html',{'blog':single_blog})
        else:
            messages.error(request,"You are not allowed to update this blog.")
            return redirect(request.META['HTTP_REFERER'])
    except:
        return redirect('my_blogs')

def delete_post(request,id):
    try:
        single_blog=Blog.objects.get(pk=id)
        if request.user.email==single_blog.author_email:
            if request.method=="POST":
                single_blog.delete()
                messages.success(request,'Blog is deleted successfully.')
                return redirect('my_blogs')
        else:
            messages.error(request,"You are not allowed to update this blog.")
            return redirect(request.META['HTTP_REFERER'])
    except Exception as e:
        messages.error(request,"Blog doesn't exists.")
        return redirect('my_blogs')

def write_post(request):
    if request.method=='POST':
        title=request.POST['title']
        subtitle=request.POST['subtitle'] 
        blog=request.POST['blog']
        try:
            banner=request.FILES['banner_image']
        except:
            banner=None
                    
        if request.user.is_authenticated:
            author=request.user.first_name
            author_email=request.user.email
        else:
            author="Anonymous"
        newBlog=Blog.objects.create(author_email=author_email,author=author,title=title,sub_title=subtitle,banner=banner,blog=blog)
        newBlog.save()
        messages.success(request,'Congrats! Your Blog is posted successfully.')
        return redirect('my_blogs')
    return render(request,'write_post.html')