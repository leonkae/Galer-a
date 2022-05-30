from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Category, Location, Image
# Create your views here.


def gallery(request):
    '''function for displaying in main pages'''
    # if statement (backend) for filter by category
    category = request.GET.get('category') 
    location = request.GET.get('location')
    categories = Category.objects.all()
    locations = Location.objects.all()
    if category == None and location==None:
        images = Image.get_images()
        return render(request, 'gallery/gallery.html',{'images':images, 'categories':categories,'locations':locations})
    else:
        if category == None and location:
            images = Image.objects.filter(location__name=location)
            print(location)
            print(images) 
        else:
            images = Image.objects.filter(category__name=category)
            print(category)
            print(images)     
        return render(request, 'gallery/gallery.html',{'images':images, 'categories':categories, 'category':category, 'locations':locations})

    

def viewPhoto(request,pk):
    '''for viewing photo'''
    images = Image.objects.get(id=pk)
    return render(request,'gallery/photo.html',{'images':images})


def search_results(request):
    '''search function'''
    if 'image' in request.GET and request.GET['image']:
        search_image = request.GET.get('image')
        searched_images = Image.search_by_category(search_image)
        message = f"{search_image}"
        print (search_image)
        return render(request,'gallery/search.html',{'searched_images':searched_images})

    else:
        message = "Did not really get that, please search again."
        return render(request,'gallery/search.html', {'message':message})
