from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
