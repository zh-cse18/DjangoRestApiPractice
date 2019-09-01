from django.contrib import admin
from django.urls import path, include
from . views import QuoteApiView , QuoteCategoryApiView

urlpatterns = [
    path('',QuoteCategoryApiView.as_view()),
    path('quotes/', QuoteApiView.as_view()),
]
