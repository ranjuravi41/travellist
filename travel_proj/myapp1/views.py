#from django.http import HttpResponse
from django.shortcuts import render
from . models import place
# Create your views here.
def demo(request):
    obj=place.objects.all()
    return render(request,"index.html",{'result':obj})
#def resultss(request):
    #num1=int(request.GET['num1'])
    #num2= int(request.GET['num2'])
    #add=num1+num2
    #sub=num1-num2
    #mul=num1*num2
    #div=num1/num2
    #return render(request,"result.html",{'addition':add,'subtraction':sub,'multiplication':mul,'division':div})
#def demo(request):
    #name="india"
    #return render(request,"indexx.html",{'obj':name})

#def about(request):
    #return render(request,"about.html")
#def contact(request):
    #return render(request,"contact.html")
#def details(request):
    #return render(request,"details.html")
#def thanks(request):
    #return HttpResponse("THANK YOU")

