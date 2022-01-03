from django.urls import path
# yo talako import chai definition based api view ko lagi ho
# from.views import article_list, article_detail,

# yo import chai class based api view ko lagi
from .views import  ArticleAPIView, ArticleDetails

urlpatterns = [

    # yo url path chai definition based api view ko lagi ho based api view
    # path('article/', article_list),
    # path('detail/<int:pk>/', article_detail),


    # yo url path chai class based api view ko lagi ho
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    
    

] 