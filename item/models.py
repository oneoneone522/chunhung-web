from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_images', blank=True, null=True)

    class Meta:
        ordering=('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='item', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='item_images',blank=True, null=True)
    model_type = models.CharField(max_length=255)
    specification=models.TextField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

