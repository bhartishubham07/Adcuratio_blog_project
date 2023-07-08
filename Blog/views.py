from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from rest_framework.response import Response
from django.views.generic import CreateView



# Create your views here.
from Blog.models import *
from Blog.forms import *
from Blog.serializers import *



def home(request):
    if request.session.get('username'):
        username = request.session.get('username')
        d={'username':username}

        return render(request,'home.html',d)
    return render(request,'home.html')


def Registeration(request):
    UFO = UserForm()
    d={'UFO':UFO}
    if request.method == 'POST':
        UFO = UserForm(request.POST)
        if UFO.is_valid():
            NUFO=UFO.save(commit=False)
            password=UFO.cleaned_data['password']
            NUFO.set_password(password)
            NUFO.save()
            return render(request, 'registeration_success.html')
        
    return render(request, 'Registeration.html', d)



def user_login(request):
    
    LFO = LoginForm()
    d ={'LFO':LFO}
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        AUO = authenticate(username=username, password=password)
        if AUO and AUO.is_active:
            login(request, AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse(home))
        
        else:
            return HttpResponse('Username or password is Invalid')

    return render(request, 'user_login.html', d)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))



@login_required
def insert_data(request):
    d={'SFO':ShoeForm()}
    if request.method =='POST' and request.FILES:
        SO = ShoeForm(request.POST,request.FILES)
        if SO.is_valid():
            SO.save()
            return render(request, 'insert_success.html')
        else:
            return render(request, 'insert_unsuccessull.html')
    
    return render(request,'insert_data.html',d)



class ShoeData(viewsets.ViewSet):
    def list(self,request):
        ADO=Shoe.objects.all()
        SJD=ShoeMS(ADO,many=True)
        d={'data':SJD.data}
        return render(request,'list.html',d)
    
    def retrieve(self,request,pk):
        SO=Shoe.objects.get(pk=pk)
        SDO=ShoeMS(SO)
        return Response(SDO.data)

    def update(self,request,pk):
        SPO=Shoe.objects.get(pk=pk)
        SPD=ShoeMS(SPO,data=request.data)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Product is updated'})
        else:
            return Response({'Failed':'Prodct is Not Updated'})
        
    
    def partial_update(self,request,pk):
        SPO=Shoe.objects.get(pk=pk)
        SPD=ShoeMS(SPO,data=request.data,partial=True)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Product is updated'})
        else:
            return Response({'Failed':'Prodct is Not Updated'})
        
    def destroy(self,request,pk):
        Shoe.objects.get(pk=pk).delete()
        return Response({'Deleted':'Product is deleted'})