from django.contrib import admin

from .models import Article                 # jun model lai admin panel ma register garni ho tyo model lai suru ma import garna parcha
 
 # Register your models here.
 
admin.site.register(Article)                #yo code le chai actually model lai admin panel ma register garne kaam garcha

