from email.mime import image
from django.shortcuts import render, redirect
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
    categories = Category.objects.all()
    
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] !='':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None 
        
        images = Image.objects.create(
            category=category,
            description=data['description'],
            location=data['location'],
            image=image,
        )  
        
        return redirect('gallery')       
            
        
    
    context = {'categories': categories}
    return render(request,'gallery/add.html', context)