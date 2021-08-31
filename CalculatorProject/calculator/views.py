from django.shortcuts import render

# Create your views here.
def Calculate(request):
    result =eval('2+4*3')
    print(result)
    return render(request,'index.html')