from django.test import TestCase
from .models import Category, Image, Location

class CategoryTestClass(TestCase):
   # Set up method
   def setUp(self):
      self.category = Category(name = 'travel')
      
   # Testing  instance
   def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))    
        
   def test_save_method(self):
      self.category.save_category()     
      categories = Category.objects.all()
      self.assertTrue(len(categories) > 0) 
      
   def test_update_category(self):
      self.category.save_category()
      self.category.name = 'fitness'
      self.category.save()
      update=Category.objects.get(name='fitness')
      self.assertEqual(update.name,'fitness')       
      

   def tearDown(self):
        Category.objects.all().delete()

   def test_delete_category(self):
      self.category.save_category()
      categories=Category.objects.all()
      self.assertEqual(len(categories),1)
      self.category.delete_category()
      del_category=Category.objects.all()
      self.assertEqual(len(del_category),0) 

class LocationTestClass(TestCase):
   # Set up method
   def setUp(self):
      self.location = Location(name = 'Dubai')
      
   # Testing  instance
   def test_instance(self):
        self.assertTrue(isinstance(self.location,Location)) 
        
   def test_save_method(self):
      self.location.save_location()     
      locations = Location.objects.all()
      self.assertTrue(len(locations) > 0)
      
   def test_update_location(self):
      self.location.save_location()
      self.location.name = 'London'
      self.location.save()
      update=Location.objects.get(name='London')
      self.assertEqual(update.name,'London')  
      
class ImageTestClass(TestCase):
   # Set up method
   def setUp(self):
      self.category = Category(name = 'travel')
      self.category2 = Category(name = 'travel')
      self.category.save()
      self.category2.save()
      self.location = Location(name = 'Kenya')
      self.location2 = Location(name = 'Kenya')
      self.location.save()
      self.location2.save()
      self.image = Image(name = 'Hot air balloon', image_description = 'this is an image', posted_date='10-10-2020', category = self.category, location = self.location)
      self.image2 = Image(name = 'Adventure Venue', image_description = 'this is a beautiful image', posted_date='10-11-2020', category = self.category2, location = self.location2)
      
   # Testing  instance
   def test_instance(self):
        self.assertTrue(isinstance(self.image,Image)) 
   def test_save_method(self):
      self.image.save()     
      images = Image.objects.all()
      self.assertTrue(len(images) > 0) 
      
   def tearDown(self):
      Image.objects.all().delete() 
      Category.objects.all().delete() 
      Location.objects.all().delete() 
        
   def test_delete_image(self):
      self.image.save()
      images=Image.objects.all()
      self.assertEqual(len(images),1)
      self.image.delete()
      del_images=Image.objects.all()
      self.assertEqual(len(del_images),0)

   def test_search_by_location(self):
      self.image.save()
      self.image2.save()
      image=Image.search_by_location('Kenya')
      self.assertEqual(len(image),2)  

   def test_search_by_category(self):
      self.image.save()
      self.image2.save()
      image=Image.search_by_category('travel')
      self.assertEqual(len(image),2) 
        

        
        
