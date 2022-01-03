from .models import Article                                                       # Article vanni model lai import garna parcha

from .serializers import ArticleSerializer                                        # AricleSerializer vanni serializer class lai pani import garna parcha

from rest_framework.response import Response                                      # hamile JsonResponse return garna ko lagi khali JsonResponse lekhi rakhna pardaina, django rest_framework le diyeko Response use gare huncha... so teskai lagi yo line import gareko

from rest_framework import status                                                 # status pani django rest_framework kai use gareko

from rest_framework import viewsets                                               # viewsets lai yesari import garna parcha

from django.shortcuts import get_object_or_404

# yo chai hami aafaile banako viewset class (i.e ArticleViewSet)
class ArticleViewSet(viewsets.ViewSet):                                           # ArticleViewSet class is inherting from ViewSet  ... yedi yesto basic ViewSet batw hamro class le inherit gari rako cha vani.. yo hamro ArticleViewSet class vitra hamile sabbai basic functionality haru (i.e list, create, retrive) lekhnai parne huncha to able to work our created viewset class
 
    def list(self, request):                                                       # yo line ko list() method handler pani django ko viewset le nai provide gareko ho
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
 
 
    def create(self, request):                                                     # yo line ko create() method handler pani django ko viewset le nai provide gareko ho
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
    def retrieve(self, request, pk=None):                                          # yedi yo line ko pk ko thau ma id use garna cha vani mathi class vitra lookup field lai id garaune # yo line ko retrieve() method handler pani django ko viewset le nai provide gareko ho
        articles = Article.objects.all()
        article = get_object_or_404(articles, pk=pk)
        serializer = ArticleSerializer(article)                                    # pk ko help batw single specific record or object nikalne vako vayera many=True nalekheko , yedi multiple records or querysets nai aako vaye many=Ture lekhna parthyo
        return Response(serializer.data)


    def update(self, request, pk=None):                                          # yedi yo line ko pk ko thau ma id use garna cha vani mathi class vitra lookup field lai id garaune # yo line ko retrieve() method handler pani django ko viewset le nai provide gareko ho
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        article = Article.objects.get(pk=pk)
        article.delete()
        return Response()
