from django.shortcuts import render
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
    else:
        form = ImageUploadForm()

    return render(request, 'droneimage/upload.html', {
        'form': form,
        "member": current_member,
    })
