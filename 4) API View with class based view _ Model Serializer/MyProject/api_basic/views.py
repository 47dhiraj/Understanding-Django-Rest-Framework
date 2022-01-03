from .models import Article                                                       # Article vanni model lai import garna parcha

from .serializers import ArticleSerializer                                        # AricleSerializer vanni serializer class lai pani import garna parcha

from rest_framework.response import Response                                      # hamile JsonResponse return garna ko lagi khali JsonResponse lekhi rakhna pardaina, django rest_framework le diyeko Response use gare huncha... so teskai lagi yo line import gareko

from rest_framework import status                                                 # status pani django rest_framework kai use gareko

from rest_framework.views import APIView                                          # yo APIView lai class based api view le inherit garne vayera yesari import gareko

# Create your views here.


# yo talako chai definition based api view ho
# @api_view(['GET', 'POST'])                                                      # using api_view               
# def article_list(request):
#     """
#     List all code articles, or create a new Article.
#     """
#     if request.method == 'GET':                                                 # yedi GET method aai rako cha vani
#         articles = Article.objects.all()                                        # yo line ko articles ma querysets haru huncha
#         serializer = ArticleSerializer(articles, many=True)                     # yedi querysets haru lai serialize garnu cha vani, many=True pani lekhna parcha
#         return Response(serializer.data)                                        # django rest_framework ko Respone return gareko i.e automatic yesle JsonResponse return garne kaam garcha
 
#     elif request.method == 'POST':                                              #yedi post method aai rako cha vani
#         serializer = ArticleSerializer(data=request.data)                       #  yedi api_view nagareko bela request batw aayeko data lai suru ma JSONParser ko help batw parse garna parthyo,, but haile api_view use gareko vayera parse garna pardaina... & arkho khyal garnu parne kura vaneko API ko case ma yedi request batw data aai rako cha vani jahile pani request.data garna parcha to obtain data coming from request
#         if serializer.is_valid():                                               # yedi serializer valid cha vani
#             serializer.save()                                                   # serializer lai save gareko
#             return Response(serializer.data, status=status.HTTP_201_CREATED)    # status pani rest_framework bata nai import garera use gareko # django rest_framework ko Respone return gareko
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # status pani rest_framework bata nai import garera use gareko  # django rest_framework ko Respone return gareko



# yo talako chai definition based api view ho
# @api_view(['GET', 'PUT', 'DELETE'])                                             # using api_view
# def article_detail(request, pk):                                                # article ko detail herna ko lagi ho yo view... url batw id or pk pani aai rako huncha
#     """
#     Retrieve, update or delete article.
#     """
#     try:
#         article = Article.objects.get(pk=pk)                                    # yedi yesari single object of instance get gareko cha query lagayera vani.. yo line ko article ko type ahile dictionary type hunch not queryset .. because single record or object dictionary data type ko huncha & mulitple records or object jahile queryset data type ho hune garcha
#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)                       # status pani django rest_framework kai use gareko  #yedi Article table ma kei record nai chaina vani 404 status return garni vaneko
 
#     if request.method == 'GET':                                                 # yedi GET Request aai rako cha vani
#         serializer = ArticleSerializer(article)                                 # ArticleSerializer class ko help batw article ma vayeko data lai serialize gareko
#         return Response(serializer.data)
 
#     elif request.method == 'PUT':                                               #yedi put or update request aai rako cha vani vaneko, 
#         serializer = ArticleSerializer(article, data=request.data)              # API request batw aayeko data lai access garda  request.data batw access garna milcha 
#         if serializer.is_valid():                                               # yedi serializer valid cha vani vaneko
#             serializer.save()                                                   # serializer lai save gareko
#             return Response(serializer.data)                                    # django rest_framework ko Response() use gareko cha
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
#     elif request.method == 'DELETE':                                            # yedi delete request aai rako cha vani
#         article.delete()                                                        # tyo article lai delete() gareko
#         return Response(status=status.HTTP_204_NO_CONTENT)                      # No content vanera 204 status pathayeko cha 
 


#yo talako chai class based api view ho

class ArticleAPIView(APIView):                                                     # ArticleAPIView() vanni class based view is inherting from APIView
 
    def get(self, request):                                                        # get request ko lagi def get(self, request):  yesari lekhincha
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)                        # querysets aaune bittikai many=True lekhna parcha
        return Response(serializer.data)
 
    def post(self, request):                                                       # post request ko lagi def post(self, request):  yesari lekhincha
        serializer = ArticleSerializer(data=request.data)                          # request batw aayeko data lai access garna ko lagi request.data nai lekhincha
        if serializer.is_valid():                                                  # serializer le check garcha request batw aayeko data valid cha ki nai vanera
            serializer.save()                                                      # serializer lai save gareko
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
 
class ArticleDetails(APIView):                                                     # ArticleDetails() vanni class based view is inherting from APIView
 
    def get_object(self, id):                                                      # Note : khyal gar jhukkelas request aai rako definition ho vani matra def get()  OR def post() OR def put() OR def delete() garni ho... but but , query run garna ko lagi definition garako cha vani definition ko name j rakhda pani huncha
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
 
 
    def get(self, request, id):                                                    # yo line ko request ko get method ma khasai kaam hudaina tei pani lekhi rakhda bigridaina
        article = self.get_object(id)                                              # mathi ko get_object() vanni method lai call gareko & thi get_object method return single record not the queryset
        serializer = ArticleSerializer(article)                                    # since article is single record not the query set so we don't need to write many=True
        return Response(serializer.data)
 

    def put(self, request, id):                                                    # yo line ko request ko chai put method ma majale kaam huncha so lekhnai parcha (i.e put request ma update garna ko lagi data aaucha)                 
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)                 # request batw aayeko data lai request.data garera access garna sakincha
        if serializer.is_valid():                                                  # yedi request batw aayeko data valid cha vani vanna khojeko
            serializer.save()                                                      # valid cha vani serializer lai save garni
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()                                                           # object or single record lai delete gareko
        return Response(status=status.HTTP_204_NO_CONTENT)

