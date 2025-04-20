from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from users.models import Member

# Create your views here.

def solarplant(request):

    current_member = Member.objects.get(member_user=request.user)

    return render(request, "mainapp/solarplant.html", {
        "member": current_member
    })