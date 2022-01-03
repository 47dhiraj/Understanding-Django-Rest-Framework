from .models import Article                                                       # Article vanni model lai import garna parcha

from .serializers import ArticleSerializer                                        # AricleSerializer vanni serializer class lai pani import garna parcha

from rest_framework.response import Response                                      # hamile JsonResponse return garna ko lagi khali JsonResponse lekhi rakhna pardaina, django rest_framework le diyeko Response use gare huncha... so teskai lagi yo line import gareko

from rest_framework import status                                                 # status pani django rest_framework kai use gareko

from rest_framework.views import APIView                                          # yo APIView lai class based api view le inherit garne vayera yesari import gareko

from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication   # django rest_framework batw Authentication lai import gareko

from rest_framework.permissions import IsAuthenticated                            # permissions batw IsAuthenticated vanni import gareko


class ArticleAPIView(APIView):                                                     # ArticleAPIView() vanni class based view is inherting from APIView
    
    #authentication_classes = [SessionAuthentication, BasicAuthentication]          # suru ma SessionAuthentication lai check garcha & then only BasicAuthentication lai check garcha
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

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
    
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

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

