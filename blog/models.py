from django.db import models
from django.utils import  timezone
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length= 250)
    content = models.TextField(max_length= 500)
    date_posted = models.DateTimeField(default= timezone.now)
    category = models.CharField(max_length= 250, default="abbreviations")
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        
        return reverse('blog-home')