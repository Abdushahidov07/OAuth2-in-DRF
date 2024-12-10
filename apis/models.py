from django.db import models


class Cars(models.Model):
    model = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    speed = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.model
    



    
