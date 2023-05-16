from django.db import models
def upload_path(instance,filename):
        return '/'.join(['products', str(instance.name),filename])
class Product(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to=upload_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField( default=1 )
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default='')
  


    def __str__(self):
        return self.name
    
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
         return self.name



class Cart(models.Model):
    customerName =models.TextField()
    productName = models.CharField(max_length=100)
    ProductQuantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=upload_path, null=True, blank=True)