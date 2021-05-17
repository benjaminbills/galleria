from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
  path('',views.index, name='index'),
  path('search/', views.search_results, name='search_results'),
  path('location/<location>', views.search_by_location, name='search_by_location'),
  path('<int:image_id>', views.detail, name='detail')
]

