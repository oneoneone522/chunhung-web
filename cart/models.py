from django.db import models

from item.models import Item

class CartItem(models.Model):
    item=models.ForeignKey(Item, related_name='quotaton', on_delete=models.CASCADE)
    specification=models.CharField(max_length=225)
    quantity=models.PositiveIntegerField(default=1)
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return f'{self.quantity} x {self.item.name}'