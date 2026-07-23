from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import JobApplication
from .forms import JobApplicationForm

# Home Dashboard View
def home(request):
    total_apps = JobApplication.objects.count()
    applied = JobApplication.objects.filter(status='Applied').count()
    interview = JobApplication.objects.filter(status='Interview').count()
    offer = JobApplication.objects.filter(status='Offer').count()
    accepted = JobApplication.objects.filter(status='Accepted').count()
    rejected = JobApplication.objects.filter(status='Rejected').count()

    context = {
        'total_apps': total_apps,
        'applied': applied,
        'interview': interview,
        'offer': offer,
        'accepted': accepted,
        'rejected': rejected,
    }
    return render(request, 'home.html', context)

# Read: List all job applications
def job_list(request):
    jobs = JobApplication.objects.all().order_by('-created_at')
    return render(request, 'jobs/list.html', {'jobs': jobs})

# Create: Add new application
def job_create(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Job application added successfully!")
            return redirect('job_list')
    else:
        form = JobApplicationForm()
    return render(request, 'jobs/create.html', {'form': form})

# Update: Edit application
def job_update(request, id):
    job = get_object_or_404(JobApplication, id=id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, "Job application updated successfully!")
            return redirect('job_list')
    else:
        form = JobApplicationForm(instance=job)
    return render(request, 'jobs/update.html', {'form': form, 'job': job})

# Delete: Confirm and delete application
def job_delete(request, id):
    job = get_object_or_404(JobApplication, id=id)
    if request.method == 'POST':
        job.delete()
        messages.success(request, "Job application deleted successfully!")
        return redirect('job_list')
    return render(request, 'jobs/delete.html', {'job': job})

# Detail: View single application details (Bonus)
def job_detail(request, id):
    job = get_object_or_404(JobApplication, id=id)
    return render(request, 'jobs/detail.html', {'job': job})