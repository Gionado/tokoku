import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    pilihan_category = [
        ('jersey', 'Jersey'),
        ('sepatu', 'Sepatu'),
        ('celana', 'Celana'),
        ('bola', 'Bola'),
        ('lain lain', 'Lain Lain'),
    ]

    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(choices=pilihan_category, default='update')
    is_featured = models.BooleanField(default = False)
    
    def __str__(self):
        return self.name
    
    # @property
    # def is_product_hot(self):
    #     return self.product_views > 20
        
    # def increment_views(self):
    #     self.product_views += 1
    #     self.save()
