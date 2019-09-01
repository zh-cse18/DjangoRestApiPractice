
from rest_framework import generics
from .serializers import QuoteSerializer, QuoteCategorySerializer
from main_app.models import QuoteCategory, Quote


class QuoteApiView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteCategoryApiView(generics.ListAPIView):
    queryset = QuoteCategory.objects.all()
    serializer_class = QuoteCategorySerializer


