from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"myapp/home.html") 

def trail(request):
    return HttpResponse("<h1>project is on air</h1>") 

def profile(request):
    name="sachin"
    return render(request,"myapp/profile.html",{'name':name})          