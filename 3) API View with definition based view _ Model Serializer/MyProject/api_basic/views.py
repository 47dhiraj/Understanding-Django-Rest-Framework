from django.shortcuts import render

from .models import Article                                                     # Article vanni model lai import garna parcha

from django.http import HttpResponse,JsonResponse                               # JsonResponse format ma view batw response pathaune parne vayeko le JsonResponse lai import gareko

from rest_framework.parsers import JSONParser                                   # Django rest_framework ko parser batw JSONParser lai import gareko

from .serializers import ArticleSerializer                                      # AricleSerializer vanni serializer class lai pani import garna parcha

from django.views.decorators.csrf import csrf_exempt                            # yedi api batw or ajax call batw view ma aauda csrf token aai rako chaina vani testo bela ma view ko just mathi @csrf_exempt vanni django le provide gareko decorator use garna parcha

from rest_framework.decorators import api_view			                        # yedi django ko rest_framework use gareko cha vani, view mwthod lai api view khalko banauna ko laig view vanda mathi view ma aaune request ko type anusar decorator lekhna parcha .. so tesko lagi yo import gareko ho

from rest_framework.response import Response                                    # hamile JsonResponse return garna ko lagi khali JsonResponse lekhi rakhna pardaina, django rest_framework le diyeko Response use gare huncha... so teskai lagi yo line import gareko

from rest_framework import status                                               # status pani django rest_framework kai use gareko

# Create your views here.

@api_view(['GET', 'POST'])                                                      # using api_view               
def article_list(request):
    """
    List all code articles, or create a new Article.
    """
    if request.method == 'GET':                                                 # yedi GET method aai rako cha vani
        articles = Article.objects.all()                                        # yo line ko articles ma querysets haru huncha
        serializer = ArticleSerializer(articles, many=True)                     # yedi querysets haru lai serialize garnu cha vani, many=True pani lekhna parcha
        return Response(serializer.data)                                        # django rest_framework ko Respone return gareko i.e automatic yesle JsonResponse return garne kaam garcha
 
    elif request.method == 'POST':                                              #yedi post method aai rako cha vani
        serializer = ArticleSerializer(data=request.data)                       #  yedi api_view nagareko bela request batw aayeko data lai suru ma JSONParser ko help batw parse garna parthyo,, but haile api_view use gareko vayera parse garna pardaina... & arkho khyal garnu parne kura vaneko API ko case ma yedi request batw data aai rako cha vani jahile pani request.data garna parcha to obtain data coming from request
        if serializer.is_valid():                                               # yedi serializer valid cha vani
            serializer.save()                                                   # serializer lai save gareko
            return Response(serializer.data, status=status.HTTP_201_CREATED)    # status pani rest_framework bata nai import garera use gareko # django rest_framework ko Respone return gareko
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # status pani rest_framework bata nai import garera use gareko  # django rest_framework ko Respone return gareko



@api_view(['GET', 'PUT', 'DELETE'])                                             # using api_view
def article_detail(request, pk):                                                # article ko detail herna ko lagi ho yo view... url batw id or pk pani aai rako huncha
    """
    Retrieve, update or delete article.
    """
    try:
        article = Article.objects.get(pk=pk)                                    # yedi yesari single object of instance get gareko cha query lagayera vani.. yo line ko article ko type ahile dictionary type hunch not queryset .. because single record or object dictionary data type ko huncha & mulitple records or object jahile queryset data type ho hune garcha
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)                       # status pani django rest_framework kai use gareko  #yedi Article table ma kei record nai chaina vani 404 status return garni vaneko
 
    if request.method == 'GET':                                                 # yedi GET Request aai rako cha vani
        serializer = ArticleSerializer(article)                                 # ArticleSerializer class ko help batw article ma vayeko data lai serialize gareko
        return Response(serializer.data)
 
    elif request.method == 'PUT':                                               #yedi put or update request aai rako cha vani vaneko, 
        serializer = ArticleSerializer(article, data=request.data)              # API request batw aayeko data lai access garda  request.data batw access garna milcha 
        if serializer.is_valid():                                               # yedi serializer valid cha vani vaneko
            serializer.save()                                                   # serializer lai save gareko
            return Response(serializer.data)                                    # django rest_framework ko Response() use gareko cha
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE':                                            # yedi delete request aai rako cha vani
        article.delete()                                                        # tyo article lai delete() gareko
        return Response(status=status.HTTP_204_NO_CONTENT)                      # No content vanera 204 status pathayeko cha 
 




