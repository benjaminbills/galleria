from django.db import models

# Create your models here.
class Image(models.Model):
  title = models.CharField(max_length=255)
  posted_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return self.name