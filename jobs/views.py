from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# View for listing all jobs
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

# View for showing job details
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})

# View for user signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('job_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
