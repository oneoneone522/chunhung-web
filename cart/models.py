from django.db import models

from item.models import Item

class Cart(models.Model):
    item=models.ForeignKey(Item, related_name='quotaton', on_delete=models.CASCADE)
    specification=models.CharField(max_length=225)
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)