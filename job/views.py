from django.shortcuts import render
from .models import JOb
from django.core.paginator import Paginator
from .forms import ApplyForm
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