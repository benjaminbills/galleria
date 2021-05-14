from django.shortcuts import render
from .models import Image
# Create your views here.
def index(request):
  images = Image.objects.all()
  print(images)
  return render(request, 'photos/index.html', {'images':images})
