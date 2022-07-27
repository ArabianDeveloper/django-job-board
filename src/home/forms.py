from django import forms
from django.forms import fields, models
from .models import *


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'
        exclude = ['image','owner']