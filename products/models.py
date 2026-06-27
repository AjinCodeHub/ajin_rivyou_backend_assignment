from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    category = models.CharField(max_length=100)
    tags = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['product_name']),
        ]
        
    def __str__(self):
        return self.product_name