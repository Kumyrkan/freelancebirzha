from django.shortcuts import render

from articals.models import Article

def articals_list(request):
    articals = Article.objects.all()
    return render(request, 'articals/articals_list.html', {'articals':articals})

# Create your views here.
