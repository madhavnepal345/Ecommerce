from django.db import models 

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.TextField(max_length=500)

    def __str__(self):
        return self.name



