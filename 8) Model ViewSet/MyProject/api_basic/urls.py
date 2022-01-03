from django.urls import path, include

from .views import ArticleViewSet                                               # jun viewset class lai import garnu parne ho tyo class lai import garne

from rest_framework.routers import DefaultRouter                                # django rest_framework routers batw DefaultRouter lai import garney


router = DefaultRouter()                                                        # creating object of a DefaultRouter
router.register('article', ArticleViewSet, basename='article')                  # khas ma yesko route path chai yesto huncha  ==> http://127.0.0.1:8000/viewset/article/     # yo line ko kaam vaneko, registering OR binding our viewset class to the router or url


urlpatterns = [

    path('viewset/', include(router.urls)),                                      # yo path chai hamro Api root path ho ( i.e  http://127.0.0.1:8000/viewset/ )                   
    path('viewset/<int:pk>/', include(router.urls)),
]