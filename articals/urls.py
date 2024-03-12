from django.urls import path, include

from articals.views import articals_list, article_detail, article_edit, article_new

urlpatterns = [
    path('', articals_list, name = 'articals_list'),
    path('<int:pk>/detail/',article_detail, name='article_detail'),
    path('<int:pk>/edit/',article_edit, name='article_edit'),
    path('new/',article_new, name='article_new'),
]
