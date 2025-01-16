from django.shortcuts import render, redirect
from .models import Product

# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")

        if name and price:
            Product.objects.create(name=name, price=price)
        return redirect("index")
    
    products = Product.objects.all()
    return render(request, "products/index.html", {"products": products})