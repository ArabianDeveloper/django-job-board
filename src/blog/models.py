from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey('Category' , related_name = 'blogs' , on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'Blog/images')
    publishde_at = models.DateTimeField(auto_now=True)
    owner_image = models.ImageField(upload_to = 'Blog/images/owners' , blank=True, null=True)
    description = models.TextField(max_length=5000)
    owner = models.ForeignKey(User , on_delete=models.CASCADE)
    About_blog_By_owner = models.TextField(max_length=300 , blank=True, null=True)
    # category = 
    instagram_feed = models.URLField(max_length=100)

    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self,*args , **kwargs):
        if not self.slug : 
            self.slug = slugify(self.title)
        else :
            self.slug = slugify(self.slug)
        self.owner_image = self.owner.profile.image
        self.About_blog_By_owner = self.owner.profile.apout
        super(Blog,self).save(*args , **kwargs)



class Comment(models.Model):
    blog = models.ForeignKey(Blog , related_name='comments' , on_delete=models.CASCADE , blank=True)
    author =  models.ForeignKey(User , on_delete=models.CASCADE)
    Photo_autor = models.ImageField(upload_to = 'comments/images')
    comment = models.TextField()
    publishde_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.blog.title)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


