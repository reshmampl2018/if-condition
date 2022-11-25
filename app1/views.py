from django.shortcuts import render

# Create your views here.
def a1_first(request):
    d={'a':1000,'b':20}
    return render(request,'a1_first.html',d)

def a1_second(request):
    d={'a':1000,'b':20,'c':3000}
    return render(request,'a1_second.html',d)
