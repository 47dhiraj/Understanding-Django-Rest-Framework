from .models import Article                                                       # Article vanni model lai import garna parcha

from .serializers import ArticleSerializer                                        # AricleSerializer vanni serializer class lai pani import garna parcha

from rest_framework import viewsets                                               # viewsets lai yesari import garna parcha




# yo talako ArticleViewSet vanni class le ModelViewSet batw inherit gari rako cha
class ArticleViewSet(viewsets.ModelViewSet):
    """
        A viewset for viewing and editing article instances.
        """

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
