from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import ProductAddForm
from django.contrib import messages
from .models import ProductDetail
from django.contrib.auth.decorators import login_required




@login_required(login_url="SignIn")
def AddCar(request):
    form = ProductAddForm()
    if request.method == "POST":
        form = ProductAddForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save()
            product.Merchant = request.user
            product.save()
            messages.info(request,"Product Added To list")
            return redirect('AddCar')

    return render(request,"addcar.html",{"form":form})


@login_required(login_url="SignIn")
def CarViewMerchant(request):
    products = ProductDetail.objects.all()
    context = {
        "products":products
    }
    return render(request,"carlist.html",context)

@login_required(login_url="SignIn")
def DeleteCar(request,pk):
    product = ProductDetail.objects.get(ProductId = pk)
    product.Product_Image.delete()
    product.delete()
    messages.info(request,"Product deleted")
    return redirect("CarViewMerchant")
    

@login_required(login_url="SignIn")
def UpdateCar(request,pk):
    product = ProductDetail.objects.filter(ProductId = pk)
    if request.method == "POST":

        pname = request.POST['pname']
        pbrand = request.POST["pbrand"]
        pdisc = request.POST["pdis"]
        pcat = request.POST["pcat"]
        price = request.POST["price"]
        image = request.FILES["image"]
        
        item = ProductDetail.objects.get(ProductId = pk)

        item.Product_Name = pname
        item.Product_Brand = pbrand
        item.Produt_Discription = pdisc
        item.Product_Price = price
        item.Product_Category = pcat
        item.Product_Image.delete()
        item.Product_Image = image
        item.save()
        messages.info(request,"Item Updated")
        return redirect('UpdateCar',pk=pk)
    context = {
        "product":product
    }
    return render(request,'update.html',context)

@login_required(login_url="SignIn")
def ViewCar(request,pk):
    product = ProductDetail.objects.filter(ProductId = pk)
    context = {
        "product":product
    }
    return render(request,"viewcar.html",context)

# Create your views here.
