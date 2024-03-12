from articals.models import Article, Category

from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Article
        fields = '__all__'