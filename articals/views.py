from django.shortcuts import render, get_object_or_404, redirect

from articals.models import Article
from articals.forms import ArticleForm

def articals_list(request):
    articals = Article.objects.all()
    return render(request, 'articals/articals_list.html', {'articals':articals})

def article_detail(request, pk):
    good = get_object_or_404(Article.objects.all(),pk=pk)
    # Good.objects.get(pk=pk)
    return render(request, 'goods/good_detail.html',{'good':good})


def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            good = form.instance
            return redirect('good_detail', pk=good.pk)
    else:
        form = ArticleForm()
    return render(request, 'goods/good_new.html', {'form':form})

def article_edit(request, pk):
    good = get_object_or_404(Article.objects.all(),pk=pk)

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=good)
        if form.is_valid():
            form.save()
            good = form.instance
            return redirect('good_detail', pk=good.pk)
    else:
        form = ArticleForm(instance=good)
    return render(request, 'goods/good_edit.html', {'form':form, 'good':good})
