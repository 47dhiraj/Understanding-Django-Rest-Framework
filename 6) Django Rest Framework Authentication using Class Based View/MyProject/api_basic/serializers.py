from rest_framework import serializers      #suru ma django ko rest_framework batw serializers lai import garney

from .models import Article                 # jun model lai serialize garney ho tyo model lai pani import garney
 
 
 
class ArticleSerializer(serializers.ModelSerializer):       # yo ArticleSerializer vanni class le ModelSerializer batw inherit gari rako cha           
   class Meta:
       model = Article
       fields ='__all__'

       # fields = ['id', 'title', 'author']               # since we are using ModelSerializer, Article model ko sabbai fields lai ArticleSerializer class ko fields ma lekhnai parcha vanne hudaina aafu lai jun jun chaincha tei matra lekhna pani paincha.. 








