from django.contrib import admin
from django.urls import path
from myapp.views import read_item

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', read_item, name='read_item'),
]