from rest_framework import serializers
from .models import *


class api_job_list(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'