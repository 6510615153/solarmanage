from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import UserRegisterForm
from .models import Member

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, "users/login.html")

def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    
    current_member = Member.objects.get(member_user=request.user)

    return render(request, "users/dashboard.html", {
        "member": current_member
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, "users/login.html", {
                "Message" : "Wrong Username or Password."
            })
        else:
            login(request, user)
            return HttpResponseRedirect(reverse("users:dashboard"))
        
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "Message" : "Logged out."
    })

def register_view(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.save()

            # Member.objects.create(
            #     member_fname = user.first_name,
            #     member_lname = user.last_name,
            #     member_user = user,
            #     member_info = "Info",
            # )

            return HttpResponseRedirect(reverse("users:login"))
        else:
            print("THIS IS WRONG")
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {
        "form": form,
        "Message" : "Register your account to gain access.",
    })

@login_required(login_url='/login')
def profile_view(request):
    current_member = Member.objects.get(member_user=request.user)
    return render(request, "users/profile.html", {
        "member": current_member
    })