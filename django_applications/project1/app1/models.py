from django.db import models

class User(models.Model) : 
    email = models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.email 
   

