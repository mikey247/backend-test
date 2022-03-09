
from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    timestamp=models.DateField(auto_now=True)


    def __str__(self):
        return f'{self.name} {self.age} {self.timestamp}'