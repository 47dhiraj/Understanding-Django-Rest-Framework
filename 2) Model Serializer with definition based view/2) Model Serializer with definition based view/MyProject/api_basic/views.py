from django.shortcuts import render

from django.http import HttpResponse,JsonResponse                   # JsonResponse format ma view batw response pathaune parne vayeko le JsonResponse lai import gareko
from rest_framework.parsers import JSONParser                       # Django rest_framework ko parser batw JSONParser lai import gareko

from .models import Article                                         # Article vanni model lai import garna parcha
from .serializers import ArticleSerializer                          # AricleSerializer vanni serializer class lai pani import garna parcha

from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt                                                     
def article_list(request):
    """
    List all code articles, or create a new Article.
    """
    if request.method == 'GET':                                     # yedi GET method aai rako cha vani
        articles = Article.objects.all()                            # yo line ko articles ma querysets haru huncha
        serializer = ArticleSerializer(articles, many=True)         # yedi querysets haru lai serialize garnu cha vani, many=True pani lekhna parcha
        return JsonResponse(serializer.data, safe=False)            #JsonResponse pathauda data chai dictionary format ma pathaunu parne ho but yedi dictionary format vanda aru format ma data pathaunu parne cha as JsonResponse vani testo senario ma safe=False ko use garnai parcha
 
    elif request.method == 'POST':                                  #yedi post method aai rako cha vani
        data = JSONParser().parse(request)                          # yo line ko JSONParser() ko kaam vaneko it parses the incoming JSON content request into python content (i.e dictionary type).     # parse ko kaam vaneko converting one type of data to another type      # yo line ko data ma finally python dictionary format ma data huncha
        serializer = ArticleSerializer(data=data)                   # dictionary data lai ArticleSeriallizer class ko help batw serialize gareko       
        if serializer.is_valid():                                   # yedi serializer valid cha vani
            serializer.save()                                       # serializer lai save gareko
            return JsonResponse(serializer.data, status=201)        # serialize gareko data lai JsonResponse ma pathako & created or save vayo vanera status 201 pani pathako cha
        return JsonResponse(serializer.errors, status=400)          # yedi error aayo vani, error status 400 as response pathakko cha



@csrf_exempt
def article_detail(request, pk):                                    # article ko detail herna ko lagi ho yo view... url batw id or pk pani aai rako huncha
    """
    Retrieve, update or delete article.
    """
    try:
        article = Article.objects.get(pk=pk)                        # yedi yesari single object of instance get gareko cha query lagayera vani.. yo line ko article ko type ahile dictionary type hunch not queryset .. because single record or object dictionary data type ko huncha & mulitple records or object jahile queryset data type ho hune garcha
    except Article.DoesNotExist:
        return HttpResponse(status=404)                             #yedi Article tale ma kei record nai chaina vani 404 status return garni vaneko
 
    if request.method == 'GET':                                     # yedi GET Request aai rako cha vani
        serializer = ArticleSerializer(article)                     # ArticleSerializer class ko help batw article ma vayeko data lai serialize gareko
        return JsonResponse(serializer.data)                        # serialize gareko data lai as a json response ko rup ma pathayeko
 
    elif request.method == 'PUT':                                   #yedi put or update request aai rako cha vani vaneko, 
        data = JSONParser().parse(request)                          # put method batw JSON data aai rako huncha so teslai JSONParser() ko help batw python dictionary data type ma lageko
        serializer = ArticleSerializer(article, data=data)          # data lai serialize gareko
        if serializer.is_valid():                                   # yedi serializer valid cha vani vaneko
            serializer.save()                                       # serializer lai save gareko
            return JsonResponse(serializer.data)                    # serializer gareko data lai json response ko rup ma pathayeko
        return JsonResponse(serializer.errors, status=400)
 
    elif request.method == 'DELETE':                                # yedi delete request aai rako cha vani
        article.delete()                                            # tyo article lai delete() gareko
        return HttpResponse(status=204)                             # HttpResponse ma status 204 halera pathayeko
 




