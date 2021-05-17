from django.shortcuts import render, get_object_or_404
from .models import Image, Location
# Create your views here.
def index(request):
  locations = Location.objects.all()
  images = Image.objects.all()
  return render(request, 'photos/index.html', {'images':images, 'locations':locations})


def detail(request, image_id):
  image = get_object_or_404(Image, pk=image_id)
  return render(request, 'photos/detail.html', {'image': image})

def search_results(request):
  if 'search' in request.GET and request.GET['search']:
      search_term = request.GET.get('search')
      searched_images = Image.search_by_category(search_term)
      message = f"{search_term}"
      return render(request, 'photos/search.html',{"message":message,"images": searched_images})

  else:
      message = "You haven't searched for any term"
      return render(request, 'photos/search.html',{"message":message})

def search_by_location(request, location):
  locations = Location.objects.all()
  images = Image.search_by_location(location)
  # images = get_object_or_404(Image, location_id=location_id)
  return render(request, 'photos/search.html',{"images": images, 'locations':locations})

