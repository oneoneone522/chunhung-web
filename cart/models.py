from django.db import models
from django.contrib.auth.models import User
from item.models import Item

class QuotationInfo(models.Model):
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100, default="Anonymous")
    phonenum=models.CharField(max_length=20, default="07-7874443")
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
        verbose_name = "Quotation Info"
        verbose_name_plural = "Quotation Infos"

    def __str__(self):
        return f"Quotation on {self.date_added}"

class QuotationItem(models.Model):
    quotation = models.ForeignKey(QuotationInfo, related_name='quoted_items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    specification = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1)
    remark = models.TextField(default='leave your remark')

    def __str__(self):
        return f"{self.item.name} ({self.quantity})"