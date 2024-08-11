from django.shortcuts import render

# Create your views here.
def Home_Page(request):
    return render(request,'index.html')
