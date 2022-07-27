from django.db import models
# Create your models here.


class Top_Companies(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'Companies/images')

    def __str__(self):
        return self.name



class Testimonial(models.Model):
    owner = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'testimonial/images')
    testimonial = models.TextField(max_length=200)
    

    def __str__(self):
        return self.owner