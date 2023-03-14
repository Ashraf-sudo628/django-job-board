from django.shortcuts import render
from .models import JOb

# Create your views here.

def job_list(resquest):
    job_list = JOb.objects.all()
    context = {'jobs' : job_list}
    return render(resquest,"job/job_list.html",context)

def job_detail(resquest, id):
    job_detail = JOb.objects.get(id = id)
    context = {'job' : job_detail}
    return render(resquest,"job/job_details.html",context)