from django shortcuts import render
from testapp.models import *

#create your views here
def index(request):
	return render(request,'testapp/m,html')

def hydjob1(request):
	jobs_list=hydjobs.objects.order_by('date')
    my_dict=('jobs_list':jobs_list)
    return render(request,'testapp/hydjobs.html',context=my_dict)

def blorejobs(request):
    return render(request,'testapp/blorejobs.html',context=my_dict)

def punejobs(request):
    return render(request,'testapp/punejobs.html',context=my_dict)


def chennaijobs(request):
    return render(request,'testapp/chennaijobs.html',context=my_dict)