from django.shortcuts import render
from blog.models import Article
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

# Create your views here.
class AllArticlesAPIView(APIView):

    def get(self, request, format=None):
        try:
            all_articles = Article.objects.published().order_by('-publish')[:5]
            data = []

            for article in all_articles:
                data.append({
                    "title": article.title,
                    "slug": article.slug,
                    "thumbnail": article.thumbnail.url if article.thumbnail else None,
                    "description": article.description,
                    "is_special": article.is_special,
                    "publish": article.publish,
                })

            return Response({'data' : data}, status=status.HTTP_200_OK)

        except:
            return Response({'status' : "خطای درون شبکه رخ داده است لطفا بعدا تلاش کنید"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class SingleArticleAPIView(APIView):
    def get(self, request, format=None):
        try:
            article_title = request.GET['article_title']
            article = Article.objects.filter(title__contains=article_title)
            serialized_data = serializers.SingleArticleSerializer(article, many=True)
            data = serialized_data.data

            return Response({'data':data}, status=status.HTTP_200_OK)

        except:
            return Response({'status': "خطای درون شبکه رخ داده است لطفا بعدا تلاش کنید"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)