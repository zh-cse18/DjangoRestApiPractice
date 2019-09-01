from django.db import models


class QuoteCategory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Quote(models.Model):
    author = models.CharField(max_length=50)
    quote = models.TextField()

    def __str__(self):
        return self.author

    def __str__(self):
        return self.quote

    quote_category = models.ForeignKey('QuoteCategory', on_delete=models.CASCADE)
