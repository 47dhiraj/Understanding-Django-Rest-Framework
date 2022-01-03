from .models import Article                                                       # Article vanni model lai import garna parcha

from .serializers import ArticleSerializer                                        # AricleSerializer vanni serializer class lai pani import garna parcha

from rest_framework import generics                                               # django rest_framework batw generics lai import gareko

from rest_framework import mixins                                                 # django rest_framework batw mixins lai import gareko  
 

 
class GenericAPIView(generics.GenericAPIView,                                     # GenericAPIView lai GenericAPIView batw inherit gari rako cha
                        mixins.ListModelMixin,                                    # ListModelMixin batw pani inherit gari rako cha # For listing your data you can use ListModelMixin
                        mixins.CreateModelMixin,                                  # yedi create garnu cha vani CreateModelMixin lai inherit garna parcha
                        mixins.UpdateModelMixin,                                  # yedi update garnu cha vani UpdateModelMixin lai inherit garna parcha
                        mixins.RetrieveModelMixin,                                # yedi retrive garnu cha vani RetrieveModelMixin lai inherit garna parcha
                        mixins.DestroyModelMixin):                                # yedi delete garnu cha vani DestroyModelMixin lai inherit garna parcha


    serializer_class = ArticleSerializer                                          # yo line ko serializer_class jun cha tyo tesari nai lekhna parcha .. django convention ho
    queryset = Article.objects.all()                                              # yo line ko queryset jasari lekheko cha tyo tesari nai lekhna parcha.. django convention ho
    lookup_field = 'id'                                                           # Note : by default lookup field ko parameter pk huncha yedi hamilai hamro lookup field(like id) rakhna cha vani lookup_field = 'id' lekhna parcha # yo line ko lookup_field jasari lekheko cha tyo tesari nai lekna parcha.. django convention ho
 
 
    def get(self, request, id = None):
 
        if id:
            return self.retrieve(request)
        else:
           return self.list(request)                                              # vaye var ko records lai list garcha
 
    def post(self, request):
        return self.create(request)                                               # post request batw aayeko data lai create(request) garera create gareko cha
 
    def put(self, request, id=None):                                              # put request batw aayeko data lai update(request, id) garera update gareko cha
        return self.update(request, id)
 
    def delete(self, request, id):                                                # delete request batw aayeko data lai destroy(request, id) garera delete gareko cha
        return self.destroy(request, id)
