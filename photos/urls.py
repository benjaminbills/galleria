from django.urls import path
from django.urls.conf import include
from . import views

#movies/
#movies/1/details
app_name = 'movies'
urlpatterns = [
  path('',views.index, name='index'),
]