from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    # cover = models.ImageField()

    datetime_dreated = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)



    def __str__(self) -> str:
        return self.title 
    
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
    