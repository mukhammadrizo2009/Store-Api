from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name