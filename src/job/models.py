from django.db import models
from django.db.models.fields import TextField
from django.utils.text import slugify
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from home.models import *
# Create your models here.

JOB_TYPE = (
    ('Full Time' , 'Full Time'),
    ('Part Time' , 'Part Time'),
)

def image_upload(instance , filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id , extension)


class Job(models.Model): # table
    owner = models.ForeignKey(User , related_name='job_owner' , on_delete=models.CASCADE)
    title = models.CharField(max_length=100) # column
    location = CountryField()
    like = models.ManyToManyField(User , blank=True)
    company = models.ForeignKey(Top_Companies , related_name = 'jobs' , on_delete=models.CASCADE)
    job_type = models.CharField(max_length=15 , choices=JOB_TYPE)
    discription = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category' , on_delete=models.CASCADE , related_name='jobs')
    image = models.ImageField(upload_to = image_upload)

    slug = models.SlugField(null=True , blank=True)

    def save(self,*args , **kwargs):
        self.slug = slugify(self.title) 
        super(Job,self).save(*args , **kwargs)


    def __str__(self):
        return self.title


class Apply(models.Model):
    job = models.ForeignKey(Job , related_name='apply_job' , on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'Applays/images')
    email = models.EmailField(max_length=255)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)


    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
