from django.db import models

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

class JOb(models.Model): #Table in DB
    title = models.CharField(max_length=100) # Column in DB
    Job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    Description = models.TextField(max_length=1000)
    Published_At = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    Salary = models.IntegerField(default=0)
    Experiance = models.IntegerField(default=1)


    def __str__(self) :
        return self.title