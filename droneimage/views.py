from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from django.conf import settings
from users.models import Member
from .models import Image
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def upload_image(request):

    current_member = Member.objects.get(member_user=request.user)
    if current_member.member_role not in ["drone", "manager"]:
        return redirect("users:unauthorized")

    if request.method == 'POST' and request.FILES['image']:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("droneimage:success")
    else:
        form = ImageUploadForm()

    return render(request, 'droneimage/upload.html', {
        'form': form,
        "member": current_member,
    })

@login_required(login_url='/login')
def success(request):
    current_member = Member.objects.get(member_user=request.user)
    if current_member.member_role not in ["drone", "manager"]:
        return redirect("users:unauthorized")
    return render(request, 'droneimage/success.html', {
        "member": current_member,
    })


