from django.urls import path, include

from api.views import ArticleList, ArticleDetail, OrderList, OrderDetail

urlpatterns = [
    path('articals/', ArticleList.as_view()),
    path('article/<int:pk>/', ArticleDetail.as_view()),
    path('orders/', OrderList.as_view()),
    path('order/<int:pk>', OrderDetail.as_view()),
]