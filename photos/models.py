from django.db import models

# Create your models here.
class Image(models.Model):
  name = models.CharField(max_length=255)
  posted_date = models.DateTimeField(auto_now_add=True)
  image_description = models.CharField(max_length=500, default='DEFAULT VALUE')
  def __str__(self):
        return self.name