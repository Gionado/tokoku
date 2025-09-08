import uuid
from django.db import models

class Product(models.Model):
    pilihan_category = [
        ('jersey', 'Jersey'),
        ('sepatu', 'Sepatu'),
        ('celana', 'Celana'),
        ('bola', 'Bola'),
        ('lain lain', 'Lain Lain'),
    ]

    name = models.CharField
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(choices=pilihan_category, default='update')
    
    def __str__(self):
        return self.title
    
    @property
    def is_news_hot(self):
        return self.news_views > 20
        
    def increment_views(self):
        self.news_views += 1
        self.save()