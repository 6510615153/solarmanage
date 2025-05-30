from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from django.conf import settings
from users.models import Member
from .models import Image
from django.http import HttpResponseRedirect

def upload_image(request):

    current_member = Member.objects.get(member_user=request.user)

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

def success(request):
    current_member = Member.objects.get(member_user=request.user)
    return render(request, 'droneimage/success.html', {
        "member": current_member,
    })


