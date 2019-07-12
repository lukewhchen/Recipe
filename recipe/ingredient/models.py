from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
# 
