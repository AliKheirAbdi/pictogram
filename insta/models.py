from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
