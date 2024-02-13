from django.urls import path, include

from articals.views import articals_list

urlpatterns = [
    path('', articals_list, name = 'articals_list')
]
