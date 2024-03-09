from django import forms

from articals.models import Article

class ArticalForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'