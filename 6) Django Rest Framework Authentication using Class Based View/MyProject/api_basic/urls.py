from django.urls import path

from .views import  ArticleAPIView, ArticleDetails

urlpatterns = [
    
    # yo url path chai class based api view ko lagi ho
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    
    

] 