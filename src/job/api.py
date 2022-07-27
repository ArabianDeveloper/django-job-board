from .serializer import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view
def job_list_api(request):
    jobs = Job.objects.all()
    data = api_job_list(jobs).data
    return Response


class JobListApi(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = api_job_list


class JobDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = api_job_list
    lookup_field = 'id'