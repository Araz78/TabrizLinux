from django.urls import path, include
from  . import views

app_name="api"
urlpatterns = [
    path('articles/all', views.AllArticlesAPIView.as_view(), name="all_articles"),
    path('article/', views.SingleArticleAPIView.as_view(), name="single-article"),
]
