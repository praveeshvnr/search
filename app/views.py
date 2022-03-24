from django.shortcuts import render
from .models import *

# Create your views here.
def name(request):
    qwer = Profile_card.objects.all()
    try:
        userid=request.POST['id']
        name = request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        place=request.POST['place']
    
        if Profile_card.objects.filter(name=name).exists():
            qwer  =   Profile_card.objects.filter(name=name)
        elif Profile_card.objects.filter(email=email).exists():
            qwer  =   Profile_card.objects.filter(email=email)  
        elif Profile_card.objects.filter(phone=phone).exists():
            qwer  =   Profile_card.objects.filter(phone=phone)  
        elif Profile_card.objects.filter(place=place).exists():
            qwer  =   Profile_card.objects.filter(place=place)  
        elif Profile_card.objects.filter(userid=userid).exists():
            qwer  =   Profile_card.objects.filter(userid=userid)  
        elif Profile_card.objects.filter(name=name,email=email,phone=phone,place=place,userid=userid).exists():
            qwer = Profile_card.objects.filter(name=name,email=email,phone=phone,place=place,userid=userid)
    except:
        
        pass
    
    return render(request, 'index.html',{'qwer':qwer})

def index(request):
    qwer = Profile_card.objects.all()
    return render(request ,'index.html',{'qwer':qwer})