from django.db import models


# Create your models here.
class Article(models.Model):
    Article = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
   
    def __str__(self):
        return self.Article
    
