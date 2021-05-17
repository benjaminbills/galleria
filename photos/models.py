from django.db import models

# Create your models here.
class Image(models.Model):
  name = models.CharField(max_length=255)
  posted_date = models.DateTimeField(auto_now_add=True)
  image_description = models.CharField(max_length=500, default='DEFAULT VALUE')
  image = models.ImageField(upload_to='images/', blank=True)
  location = models.ForeignKey('Location', on_delete=models.CASCADE, default=0)
  category = models.ForeignKey('Category', on_delete=models.CASCADE, default=0)
  
  def __str__(self):
        return self.name
  @classmethod
  def search_by_category(cls,search_term):
        images = cls.objects.filter(category__name__contains=search_term)
        return images
  
  @classmethod
  def search_by_location(cls,search_term):
        images = cls.objects.filter(location__name__contains=search_term)
        return images
  
  @classmethod
  def get_image_by_id(cls,id):
        image=cls.objects.get(id=id)
        return image 
  
class Location(models.Model):
  name = models.CharField(max_length=255)
  #magic method
  def __str__(self): 
    return self.name

  def save_location(self):
      self.save()      
      
  def delete_location(self):
      self.delete()  
  

class Category(models.Model):
  name = models.CharField(max_length=255)
  #magic method
  def __str__(self): 
    return self.name
  
  def save_category(self):
      self.save()      
      
  def delete_category(self):
      self.delete()  