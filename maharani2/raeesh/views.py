from django.shortcuts import render
from .models import Bhai
from .forms import baby


# Create your views here.
def rom(request):
       if request.method=='POST':
              cm=baby(request.POST)
              if cm.is_valid():
                     nm=cm.cleaned_data['name']
                     tt=cm.cleaned_data['roll']
                     sm=Bhai.objects.filter(name=nm,roll=tt)
                     return render(request,'new/home.html',{'fight':sm})
       else:

             cm=baby()
       return render(request,'new/maha.html',{'form':cm})
      

