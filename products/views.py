from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 3) # Show 3 contacts per page
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
 
    return render(request, "products.html", {"products": products})
    
def view_specific_product(request, id):
    products = Product.objects.all()
    return render(request, "product.html")