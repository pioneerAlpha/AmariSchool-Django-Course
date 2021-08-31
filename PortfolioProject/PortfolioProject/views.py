from django.shortcuts import render
from database.models import Testimonial
from django.contrib.auth.models import User,auth

def Home(request):
    persons=Testimonial.objects.all()


    # person1=Testimonial('img/testimonials/testimonials-5.jpg',4.9,'Samiur Abir','Freelancer',' Proin iaculis purus consequat sem cure digni ssim donec porttitora entum suscipit rhoncus. Accusantium quam, ultricies eget id, aliquam eget nibh et. Maecen aliquam, risus at semper.')
    # person2=Testimonial('img/testimonials/testimonials-5.jpg',2.9,'Amlan','Freelancer',' Proin iaculis purus consequat sem cure digni ssim donec porttitora entum suscipit rhoncus. Accusantium quam, ultricies eget id, aliquam eget nibh et. Maecen aliquam, risus at semper.')
    # person3=Testimonial('img/testimonials/testimonials-5.jpg',3.5,'Fahim','Freelancer',' Proin iaculis purus consequat sem cure digni ssim donec porttitora entum suscipit rhoncus. Accusantium quam, ultricies eget id, aliquam eget nibh et. Maecen aliquam, risus at semper.')
    # person4=Testimonial('img/testimonials/testimonials-5.jpg',4.2,'Huzaifa','Freelancer',' Proin iaculis purus consequat sem cure digni ssim donec porttitora entum suscipit rhoncus. Accusantium quam, ultricies eget id, aliquam eget nibh et. Maecen aliquam, risus at semper.')
   
    # personList=[person1,person2,person3,person4]
    # for person in personList:
    #     if person.rating <3:
    #         personList.remove(person)
    
    try :
        with open('input.txt') as files:
            file_read=files.read()
        print('File is there.')
    except FileNotFoundError:
        print('File not found.')
    finally:
        print('Finally block executed')


    return render(request,'index.html',{'testimonials':persons})

def Registration(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
            user.save()
            return render(request,'login.html')
        else:
            render(request,'registration.html')

        
    return render(request,'registration.html')

def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,'dashboard.html')
        else:
            return render(request,'login.html')


    return render(request,'login.html')

def Logout(request):
    if request.method=='POST':
        auth.logout(request)
        return render(request,'login.html')

def Dashboard(request):
    if not request.user.is_authenticated:
        return render(request,'login.html')
        
    return render(request,'dashboard.html')

