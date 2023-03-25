from django.shortcuts import render
from .models import JOb
from django.core.paginator import Paginator
# Create your views here.

def job_list(resquest):
    job_list = JOb.objects.all()

    paginator = Paginator(job_list, 1)
    page_number = resquest.GET.get('page')
    page_obj = paginator.get_page(page_number)



    context = {'jobs' : page_obj}
    return render(resquest,"job/job_list.html",context)

def job_detail(resquest, id):
    job_detail = JOb.objects.get(id = id)
    context = {'job' : job_detail}
    return render(resquest,"job/job_details.html",context)