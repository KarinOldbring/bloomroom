from django.shortcuts import render
from .models import Product

def all_products(request):
    """
    View to sort all products, including sorting and searching
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

