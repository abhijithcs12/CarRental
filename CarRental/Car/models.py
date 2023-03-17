from django.db import models
from django.contrib.auth.models import User


class ProductDetail(models.Model):

    option = (
        ("Suv","Suv"),
        ("Hatchback","Hatchback"),
        ("Croosover","Croosover")
        )

    ProductId = models.AutoField(primary_key=True)
    Product_Name = models.CharField(max_length=255)
    Product_Brand = models.CharField(max_length=255)
    Produt_Discription = models.CharField(max_length=1000)
    Product_Price = models.IntegerField()
    Product_Category = models.CharField(max_length=255,choices=option)
    Product_Image = models.ImageField(upload_to="product_image")
    
    Merchant = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)


# Create your models here.
