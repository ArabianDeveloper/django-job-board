from django.core import paginator
from django.shortcuts import redirect, render
from .models import *
from django.core.paginator import Paginator
from .forms import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import *
# Create your views here.

def job_list(request):
    job_list = Job.objects.all()

    ## filters
    myfilter = JobFilter(request.GET , queryset=job_list)
    job_list = myfilter.qs

    paginator = Paginator(job_list , 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)



    context = {
        'jobs':page_obj,
        'j':job_list,
        'myfilter':myfilter,
    }
    return render(request , 'job/job_list.html' , context)




def job_detail(request , slug):
    job_detail = Job.objects.get(slug = slug)

    if request.method == 'POST':
        form = ApplyForm(request.POST , request.FILES)
        print('test')
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
            print('done')
    else:
        form = ApplyForm()


    context = {
        'job' : job_detail,
        'form' : form,
    }
    return render(request , 'job/job_detail.html' , context)

def like(request , slug):
    job_detail = Job.objects.get(slug = slug)
    if request.user in job_detail.like.all():
        job_detail.like.remove(request.user)
    else:
        job_detail.like.add(request.user)


    return redirect(reverse('job:job_list'))
    


@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))

    else:
        form = JobForm

    context = {
        'form':form
    }

    return render(request , 'job/add_job.html' , context)


