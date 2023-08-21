from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CreateUserForm,CustomerForm,OrderForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
def home(request):
    last_five_orders=Order.objects.all().order_by('-date_created')[:5]
    orders=Order.objects.all()
    total_orders=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()
    context={'last_five_orders':last_five_orders,'total_orders':total_orders,'delivered':delivered,'pending':pending}
    return render(request, 'accounts/dashboard.html',context)

def product(request):
    return render(request, 'accounts/product.html')

@login_required(login_url='login')
def customer(request):
    customer_instance=request.user.customer
    form=CustomerForm(instance=customer_instance)
    context={'form':form}
    
    if request.method=='POST':
        form= CustomerForm(request.POST, request.FILES, instance=customer_instance)
        if form.is_valid():
            form.save()
            
    return render(request, 'accounts/customer.html',context)
                  
def register(request):
    form =CreateUserForm()
    if request.method=='POST':
        # username=request.POST.get('username')
        # email=request.POST.get('email')
        # password1=request.POST.get('password1')
        # password2=request.POST.get('password2')
        # print(username,email, password1, password2)
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request, 'accounts/register.html',context)

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user =authenticate(request,username=username, password=password)
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,"Username or passowrd in wrong.")
        
    return render(request, 'accounts/login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def product(request):
    products=Product.objects.all()
    return render(request, 'accounts/products.html',{'products':products})

@login_required(login_url='login')
def order(request):
    orders=Order.objects.all()
    return render(request, 'accounts/orders.html',{'orders':orders})

@login_required(login_url='login')
def userpage(request):
    
    orders=request.user.customer.order_set.all()
    total_orders=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()
    context={'orders':orders,'total_orders':total_orders,'delivered':delivered,'pending':pending}
    return render(request,'accounts/user.html',context)

@login_required(login_url='login')
def updateOrder(request,pk):
    order= Order.objects.get(id=pk)
    
    form=OrderForm(instance=order)
    
    if request.method == 'POST':
        form =OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order')
    context={'form':form}
    return render(request,'accounts/update_order_form.html',context)

@login_required(login_url='login')
def deleteOrder(request,pk):
    order= Order.objects.get(id=pk)
    
    if request.method == 'POST':
        order.delete()
        return redirect('order')
    context={'item':order}
    
    return render(request, 'accounts/delete.html',context)