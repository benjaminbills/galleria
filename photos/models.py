from django.db import models

# Create your models here.
class Image(models.Model):
  name = models.CharField(max_length=255)
  posted_date = models.DateTimeField(auto_now_add=True)
  image_description = models.CharField(max_length=500, default='DEFAULT VALUE')
  location = models.ForeignKey('Location', on_delete=models.CASCADE)
  category = models.ForeignKey('Category', on_delete=models.CASCADE)
  
  def __str__(self):
        return self.name

class Location(models.Model):
  name = models.CharField(max_length=255)
  #magic method
  def __str__(self): 
    return self.name

class Category(models.Model):
  name = models.CharField(max_length=255)
  #magic method
  def __str__(self): 
    return self.name