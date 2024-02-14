from django.shortcuts import render

# Create your views here.
def cham(request):
    return render(request,'cham.html')

def champ(request):
    return render(request,'champ.html')

def chamu(request):
    return render(request,'chamu.html')

def sam(request):
    return render(request,'sam.html')
