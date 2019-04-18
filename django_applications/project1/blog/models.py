from django.db import models
from django.contrib.auth.models import User 

class Story(models.Model) : 
    author = models.ForeignKey(to=User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    topic = models.CharField(max_length=50)
    content = models.TextField()
    def __str__(self):
        return self.title

