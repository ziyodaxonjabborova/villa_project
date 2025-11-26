from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)  
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Property(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    location = models.CharField(max_length=200)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    area = models.IntegerField(help_text='m2')
    floor = models.IntegerField()
    parking = models.CharField(max_length=50)
    image = models.FileField(upload_to='images/')
    featured_deal = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



