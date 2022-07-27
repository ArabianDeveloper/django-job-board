import django_filters
from .models import *

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains' , label='Name')
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['published_at','image','salary','vacancy','slug','owner','discription','like']
