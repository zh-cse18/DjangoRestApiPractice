from django.contrib import admin
from . models import QuoteCategory, Quote


class BlogPostFilter(admin.ModelAdmin):
    list_filter = ['title']


admin.site.register(QuoteCategory,BlogPostFilter)

class BlogPostQuote(admin.ModelAdmin):
    list_display = ['author', 'quote']
    list_filter = ['author', 'quote']

admin.site.register(Quote,BlogPostQuote)