from django.db import models

# Create your models here.

class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    photo_url = models.URLField()
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name