from django.db import models
from django.utils import  timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length= 250)
    content = models.TextField(max_length= 5000)
    date_posted = models.DateTimeField(default= timezone.now)
    category = models.CharField(max_length= 250, default="abbreviations")
    

    def __str__(self):
        return self.title
    
