from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Contactus, Record

# Create your views here.
def home(request):
    if request.method == 'POST':
        fm = Contactus(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            ph = fm.cleaned_data['phone']
            em = fm.cleaned_data['email']
            msg = fm.cleaned_data['message']
            print('Name:',nm)
            print('Phno:',ph)
            print('Email:',em)
            print('Message:',msg)
            reg = Record(name=nm, phone=ph, email=em, message=msg)
            reg.save()
            fm = Contactus()   
            print("POST1")  

    else:
        print("GET1")
        fm = Contactus()
    dat = Record.objects.all()

    return render(request, 'core/index.html', {'form' : fm, 'data': dat})

def delete_data(request,id):
    if request.method == 'POST':
        pi = Record.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
