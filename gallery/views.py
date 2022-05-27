from django.shortcuts import render
from .models import Category, Location, Image
# Create your views here.

def gallery(request):
    categories =  Category.objects.all()
    images = Image.objects.all()
    locations = Location.objects.all()
    
    context = {'categories': categories,'images':images,'locations':locations}
    
    return render(request, 'gallery/gallery.html',context )

def viewPhoto(request,pk):
    images = Image.objects.get(id=pk)
    
    return render(request,'gallery/photo.html',{'images':images})

def addPhoto(request):
    return render(request,'gallery/add.html')