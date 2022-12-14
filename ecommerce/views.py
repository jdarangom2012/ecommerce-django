from django.shortcuts import render
from django.urls import is_valid_path
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_avail = True)
    context = {
        'products' : products,       
    }

    return render(request, 'home.html', context)

