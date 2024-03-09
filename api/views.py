from django.shortcuts import render, get_object_or_404
from articals.models import Article
from articals.serializers import ArticleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AricleList(APIView):

    def get(self, request):
        obj = Article.objects.all()
        serializer = ArticleSerializer(obj, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetail(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(Article.objects.all(), pk=pk)
        serializer = ArticleSerializer(obj)
        return Response(serializer.data)
    
    def put(self, request, pk):
        obj = get_object_or_404(Article.objects.all(), pk=pk)
        serializer = ArticleSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = get_object_or_404(Article.objects.all(), pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
