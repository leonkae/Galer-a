from unicodedata import category
from django.test import TestCase
from .models import Category, Location, Image

class ImageTestClass(TestCase):
    '''tests for Image class'''
    
    def setUp(self):
        self.category = Category(name='random')
        self.category.save()
        self.location = Location(name='kajiado')
        self.location.save()
        self.image = Image(image='name.jpg', name="name", description="description is a description", category=self.category, location=self.location)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
        
    def test_save_method(self):
        self.image.save()
        image = Image.get_images()
        self.assertTrue(len(image)>0) 
               
class CategoryTestclass(TestCase):
    '''tests for Category'''
    
    def setUp(self):
        self.category = Category(name='random')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))   
        
    def tearDown(self):
        Category.objects.all().delete    
    
    def test_get_category(self):
        self.category.save()
        category = Category.objects.all()
        self.assertTrue(len(category),1)
        
    def test_filter_category(self):
        self.category.save()
        categories = Category.objects.filter()
        self.assertTrue(len(categories))   
        
        
class LocationTestclass(TestCase):
    '''tests for Location'''        
    def setUp(self):
        self.location =Location(name='kajiado')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))    
        
    def tearDown(self):
        Category.objects.all().delete
        
    def test_get_category(self):
        self.location.save()
        location = Location.objects.all()
        self.assertTrue(len(location),1)    
        
    def test_filter_location(self):
        self.location.save()
        locations = Location.objects.filter()
        self.assertTrue(len(locations))      
        
        
        
        
                    