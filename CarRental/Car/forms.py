from django.forms import ModelForm
from .models import ProductDetail

class ProductAddForm(ModelForm):
    class Meta:
        model = ProductDetail
        fields = ["Product_Name","Product_Brand","Produt_Discription","Product_Price","Product_Category","Product_Image"]
