from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField



class ActiveCommentsManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(verbose_name=_('Product Image'), upload_to='product/product_cover/', blank=True)


    datetime_dreated = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)



    def __str__(self) -> str:
        return self.title 
    
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
    


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
    ]

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(verbose_name=_('Comment Text'))
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name=_('What is your score?'))
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    

    # Manager
    objects = models.Manager()
    active_comments_manager = ActiveCommentsManager()


    def get_absolute_url(self):
        return reverse("product_detail", args=[self.product.id])
    



