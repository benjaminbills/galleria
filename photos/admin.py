from django.contrib import admin
from .models import Image,Category,Location
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
  filter_horizontal=('categorys')

admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)