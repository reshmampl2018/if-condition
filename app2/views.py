from django.shortcuts import render

# Create your views here.
def a2_first(request):
    d={'a':1000,'b':20,'c':3000}
    return render(request,'a2_first.html',d)

def a2_second(request):
    d={'name':'reshu'}
    return render(request,'a2_second.html',d)
