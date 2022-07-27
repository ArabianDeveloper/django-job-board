from django.urls import path
from . import views
from . import api

app_name = 'job'

urlpatterns = [
    path('' , views.job_list , name='job_list'),
    path('add' , views.add_job , name = 'add_job'),
    path('<str:slug>' , views.job_detail , name = 'job_detail'),
    path('<str:slug>/like' , views.like , name = 'like'),


    # api
    path('api/c/jobs' , api.JobListApi.as_view()),
    path('api/c/jobs/<int:id>' , api.JobDetailApi.as_view()),
    
]



