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
        
    
        

        
        
