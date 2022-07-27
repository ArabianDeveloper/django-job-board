from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from accounts.models import *
from .forms import *
from .filters import *
# Create your views here.

def blog(request):
    blog = Blog.objects.all()
    category = Category.objects.all()

    myfilter = BlogFilter(request.GET , queryset=blog)
    blog = myfilter.qs

    paginator = Paginator(blog , 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'blogs':page_obj,
        'cts':category,
        'myfilter':myfilter,
        
    }
    return render(request , 'blog.html' , context)


def single_blog(request , slug):
    blog = Blog.objects.get(slug = slug)
    if request.method == 'POST':
        profile = Profile.objects.get(user = request.user)
        form = CommentForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.blog = blog
            myform.author = request.user
            myform.Photo_autor = profile.image
            myform.save()

    else:
        form = CommentForm()

    
    blogs = Blog.objects.all()
    category = Category.objects.all()
    context = {
        'blog':blog,
        'blogs':blogs,
        'cts':category,
        'form':form,
    }
    return render(request , 'single-blog.html' , context)


def new(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user = request.user)
        form = BlogForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.owner_image = profile.image
            myform.save()

    else:
        form = BlogForm()
    context = {
        'form':form
    }

    return render(request , 'NBlog.html' , context)