from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    caption = models.TextFieldField()
    created_date = models.DateTimeField(default=timezone.now)