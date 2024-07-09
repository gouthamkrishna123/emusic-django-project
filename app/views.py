from django.shortcuts import render,redirect
from django.core.paginator import Paginator
# Create your views here.
from app.models import customer, Album, Songs
from app.models import music

# Create your views here.
def welcome(request):
    if "username" in request.session:
        current_user=request.session["username"]
        return render(request,"welcome.html",{"current_user":current_user})
    return render(request,"welcome.html")
def login(request):
    if request.method=="POST":
        uname=request.POST['usname']
        passw=request.POST['password']
        details=customer.objects.filter(username=uname,password=passw)
        if details:
            request.session["username"]=uname
            return redirect('index')
        else:
            print("Invalid")
            return render(request,'signup.html')

    return render(request,"login.html")
def signup(request):
    if request.method=="POST":
        uname=request.POST['username']
        name=request.POST['name']
        password=request.POST['password']
        conformpassword=request.POST['conpassword']
        age=request.POST['age']
        email=request.POST['emailid']
        customer(username=uname,name=name,password=password,conformpassword=conformpassword,age=age,email=email).save()
        return render(request,"welcome.html")
    return render(request,"signup.html")
def logout(request):
    del request.session["username"]
    return render(request,"welcome.html")

def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def blog(request):
    return render(request,"blog.html")
def contact(request):
    return render(request,"contact.html")
def elements(request):
    return render(request,"elements.html")
def gopi(request):
    return render(request,"gopi.html")

def music(request):
    album=Album.objects.all()
    return render(request,"music.html",{"album":album})

def new(request):
    return render(request,"new.html")


def playlist (request):
    album_name = request.GET.get("album")
    songs_list = Songs.objects.filter(album_name=album_name)
    paginator=Paginator(songs_list, 1)
    page_number = request.GET.get('page')
    songs_page=paginator.get_page(page_number)
    return render(request, "playlist.html", {"songs_page": songs_page, "album_name": album_name})

