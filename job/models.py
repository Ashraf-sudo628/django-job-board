from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.

'''
we use django model field as it give ue 
    - html widget
    - validation
    - db size
'''

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)


def Image_upload(instance,filename):
    Imagename , extention = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extention)

class JOb(models.Model): #Table in DB
    Owner = models.ForeignKey(User, verbose_name=("Job_owner"), on_delete=models.CASCADE)
    title = models.CharField(max_length=100) # Column in DB
    Job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    Description = models.TextField(max_length=1000)
    Published_At = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    Salary = models.IntegerField(default=0)
    Experiance = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=Image_upload)
    slug = models.SlugField(blank=True , null=True)


    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(JOb,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    Name = models.CharField(max_length=25)

    def __str__(self):
        return self.Name


class Apply(models.Model):
    job = models.ForeignKey(JOb, verbose_name=("apply_job"), on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    Email =models.EmailField(max_length=254)
    Website = models.URLField(max_length=200)
    CV = models.FileField(upload_to='apply/')
    Cover_Litter = models.TextField(max_length=500)
    Created_At = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name
