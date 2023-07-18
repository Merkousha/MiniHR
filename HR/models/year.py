from HR import models
from django.db import models

class Year(models.Model):
    # refrence = models.ForeignKey(Refrence, on_delete=models.CASCADE,default=1)   
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name