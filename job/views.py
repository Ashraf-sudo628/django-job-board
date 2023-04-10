
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import JOb
from django.core.paginator import Paginator
from .forms import ApplyForm , AddJobForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def job_list(resquest):
    job_list = JOb.objects.all()

    paginator = Paginator(job_list, 4)
    page_number = resquest.GET.get('page')
    page_obj = paginator.get_page(page_number)



    context = {'jobs' : page_obj}
    return render(resquest,"job/job_list.html",context)

def job_detail(resquest, slug):
    job_detail = JOb.objects.get(slug=slug)
    if resquest.method =='POST':
        form =ApplyForm(resquest.POST,resquest.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
    else:
        form = ApplyForm   

    context = {'job' : job_detail,'applyform':form}
    return render(resquest,"job/job_details.html",context)


@login_required
def add_job(resquest):
    if resquest.method == 'POST':
        form = AddJobForm(resquest.POST,resquest.FILES)
        if form.is_valid():
            myForm = form.save(commit=False)
            myForm.Owner = resquest.user
            myForm.save()
            return redirect(reverse('jobs:job_list',))
    else:
        form = AddJobForm
    
    return render(resquest,"job/add_job.html",{'addform':form})