from django.shortcuts import render,HttpResponseRedirect
from .models import Vidyarthi
from .forms import StudentData

# Create your views here.
def Show(request):
    if request.method=='POST':
        st = StudentData(request.POST)
        if st.is_valid():
            st.save()
            st = StudentData()
    else:   
        st = StudentData()
    information = Vidyarthi.objects.all()
    return render(request,'home.html',context={'form':st,'info':information})


def update(request,id):
    if request.method == 'POST':
        infomation = Vidyarthi.objects.get(pk=id)
        st = StudentData(request.POST,instance=infomation)
        if st.is_valid():
            st.save()
            st = StudentData()
    else:
        infomation = Vidyarthi.objects.get(pk=id)
        st = StudentData(instance=infomation) 
    return render(request,'update.html',context={'form':st})


def delete (request, id):
    if request.method == 'POST':
        st = Vidyarthi.objects.get(pk=id)
        st.delete()
    return HttpResponseRedirect('/')