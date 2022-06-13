from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField(null=True)
    description = models.TextField(null=True, blank=True)
    dateAdded = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(null=True)
    

    def __str__(self):
        return self.name