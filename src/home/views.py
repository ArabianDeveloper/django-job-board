from job.filters import *
from home.models import Top_Companies
from django.shortcuts import render
from job.models import *
from django.core.paginator import Paginator
from accounts.models import *
from .models import *
from .forms import *
# Create your views here.


def index(request):
    job_list = Job.objects.all()
    apply_list = Apply.objects.all()
    category = Category.objects.all()
    companies = Top_Companies.objects.all()
    testimonial = Testimonial.objects.all()
    myfilter = JobFilter(request.GET , queryset=job_list)
    j = Job.objects

    if request.method == 'POST':
        profile = Profile.objects.get(user = request.user)
        form = TestimonialForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user.username
            myform.image = profile.image
            myform.save()
    else:
        form = TestimonialForm()



    context = {
        'j':job_list,
        'a':apply_list,
        'cats':category,
        'companys':companies,
        'test':testimonial,
        'form':form,
        'jc':j,
        'myfilter':myfilter.form,
    }
    return render(request , 'home.html' ,context)


def candidate(request):
    apply_list = Apply.objects.all()
    paginator = Paginator(apply_list , 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'a':page_obj,
    }

    return render(request , 'candidate.html' , context)    