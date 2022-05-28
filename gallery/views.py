from django.shortcuts import render, redirect
from .models import Category, Location, Image
# Create your views here.

def gallery(request):
    categories =  Category.objects.all()
    images = Image.get_images()
    locations = Location.objects.all()
    
    # context = {'categories': categories,'images':images,'locations':locations}
    
    
    
    return render(request, 'gallery/gallery.html',{'images':images,'locations':locations, 'categories':categories})

def viewPhoto(request,pk):
    images = Image.objects.get(id=pk)
    
    return render(request,'gallery/photo.html',{'images':images})

