from django.db import models 


# Create your models here.

class Category(models.Model):
    '''category model'''
    name = models.CharField(max_length=100, null=False, blank=False)    
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    '''location model'''
    name = models.CharField(max_length=100, null=False, blank=False)    
    
    def __str__(self):
        return self.name  
class Image(models.Model):
    '''image model'''
    image = models.ImageField(upload_to= 'media/', default='')
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    location =  models.ForeignKey(Location, on_delete=models.SET_NULL , null=True)
    
    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images
    
    @classmethod
    def search_by_category(cls,category):
        images = cls.objects.filter(category__name=category)
        return images
    
    
    
    def __str__(self):
        return self.description
    

    
    
    

    