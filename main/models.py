from django.db import models

class Accordion(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()
    
    def __str__(self):
        return self.title
    
    
class Featured_House(models.Model): 
    villa=models.ForeignKey("Villa",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.villa.name
    
    
class Category(models.Model):  
    name=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
  
    
class PaymentType(models.Model):
    name=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Villa(models.Model):
    image=models.FileField(upload_to="images")
    name=models.CharField(max_length=200)
    desc=models.TextField()
    category=models.ForeignKey("Category",on_delete=models.CASCADE,related_name="villas")
    price=models.DecimalField(max_digits=20,decimal_places=3)
    area=models.DecimalField(max_digits=7,decimal_places=2)
    floor=models.PositiveIntegerField(default=1)
    bedroom=models.PositiveIntegerField(default=2)
    bathroom=models.PositiveIntegerField(default=2)
    parking=models.PositiveIntegerField(default=2)
    payment_type=models.ForeignKey("PaymentType",on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name




    