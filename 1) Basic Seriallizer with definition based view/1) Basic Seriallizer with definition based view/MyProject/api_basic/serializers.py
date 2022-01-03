from rest_framework import serializers      #suru ma django ko rest_framework batw serializers lai import garney

from .models import Article                 # jun model lai serialize garney ho tyo model lai pani import garney
 
 
 
class ArticleSerializer(serializers.Serializer):            # ArticleSerializer class vanni hami aafaile banako auta serializer class ho & this class is now inheriting from Serializer # Note: Yedi Serializer matra batw import gareko cha vani, testo case ma, hamro model ma vayeko sabbai fields lai yo hamile banayeko serializer class ma lekhna parcha... yedi ModelSerializer use gareko vaye model ko sabbai fields lekhna pardaina thyo
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()



    # Note : ahile hamile Serializer batw import garera yo ArticleSerializer class banako vayera create & update vanni definition banauna parcha.. yedi ModelSerializer use gareko vaye yo banauna pardaina thyo
    def create(self, validated_data):               # Note : jaba hami ArticleSerialier class ko kunai naya object or instance banayera tesma value rakhera or narakhi kana save() garchau(i.e obj.save() call garchau) , teti bela yo create() vanni method call hune garcha
        # Create and return a new `Article` instance, given the validated data.

        return Article.objects.create(validated_data)
 
 
    def update(self, instance, validated_data):
        #Update and return an existing `Article` instance, given the validated data.
 
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()         #saving instance
        return instance            # returning instance





