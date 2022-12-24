from django.shortcuts import render
from . import models


# Create your views here.
def home(request):
    store_name=["lapis.co"]
    # brand=['apple','Dell','HP','Microsoft','asus','acer','Lenovo']
    # ram=[4,8,12,16,32,64,128]
    # hdd=[256,512,1024,'1.5tb','2tb','2.5tb','3tb']
    # ssd=[256,512,1024,'1.5tb','2tb','2.5tb','3tb']
    # processer=['intel i3','intel i5','intel i7','intel i9','AMD 5','AMD 7','AMD']
    # price=['40k','50k','60k','70k','80k','90k','100k']
    # data=zip(brand,ram,hdd,ssd,processer,price)
    
    data= models.LaptopData.objects.all
    context={
        'data':data
    }
    return render(request,'home.html',context)
def info(request):
    data=models.discription.objects.all()
    print(data[0].p_id)
    context={
        'data':data
    }
    
    return render(request, "info.html", context)
    