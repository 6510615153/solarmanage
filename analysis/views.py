from django.shortcuts import render, redirect
from .forms import ReportUploadForm
from django.conf import settings
from users.models import Member
from .models import Report
from mainapp.models import SolarPlant

def upload_report(request):

    current_member = Member.objects.get(member_user=request.user)

    if request.method == 'POST':
        form = ReportUploadForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.writer = current_member
            obj.save()
            return redirect("analysis:success")
    else:
        form = ReportUploadForm()

    return render(request, 'analysis/upload.html', {
        'form': form,
        "member": current_member,
    })

def success(request):
    current_member = Member.objects.get(member_user=request.user)
    return render(request, 'analysis/success.html', {
        "member": current_member,
    })

def details(request, report_id):
    current_report = Report.objects.get(id=report_id)
    # plant = SolarPlant.objects.get(id=current_report.solarplant.id)
    # current_image = plant.get_latest_image()
    
    return render(request, "analysis/details.html", {
        "report": current_report,
        'pic': current_report.image,
    })
