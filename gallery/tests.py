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
               
