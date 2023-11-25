from django.db import models

# Create your models here.
class Members(models.Model):
    name = models.CharField(max_length=100)
    f_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.name} - {self.username}'
