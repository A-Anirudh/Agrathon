from django.db import models
from authentication.models import CustomUser
class Farmer(models.Model):
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    phone_number = models.IntegerField(max_length=10)
    email = models.EmailField(max_length=254)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name.username
class Crop(models.Model):
    farmer_name = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    crop_name = models.CharField(max_length=50)
    stock = models.IntegerField()
    cost = models.IntegerField()

    def __str__(self):
        return f"{self.crop_name} from {self.farmer_name.name}"


class Customer(models.Model):
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=254)
    city = models.CharField(max_length=50)
    def __str__(self):
        return self.name.username


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    qty = models.IntegerField()
    # Order ID is the built in ID in django models
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    total_price = models.FloatField(default=0,blank=True,null=True)

    def __str__(self):
        return f"ID - {self.id} for {self.customer.name}"
    

class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title
